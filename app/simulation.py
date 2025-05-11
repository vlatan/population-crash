import time
import random
import pandas as pd
import streamlit as st

from . import config
from . import utils as ut
from . import population as pop
from . import reproduction as rep


def simulate() -> dict[str, config.Vector] | None:
    """
    Records the relevant numbers after every cycle.
    Returns the numbers for each population category in a dict.
    """

    # get ready made dataframe from CSV file just for the initial page load display
    placeholder_df = ut.read_placeholder_csv()

    st.subheader("Simulation Chart")
    st.write(
        """
        Press **the button in the sidebar** to run the simulation. The chart will re-render
        showing the updated population numbers.
        """
    )

    chart_placeholder = st.empty()
    chart_placeholder.line_chart(placeholder_df, height=500, use_container_width=True)

    st.subheader("Simulation Table")
    st.write(
        """
        Press **the button in the sidebar** to run the simulation. The table will re-render
        showing the updated population numbers.
        """
    )

    table_placeholder = st.empty()
    table_placeholder.dataframe(placeholder_df, use_container_width=True)

    excerpt, info = ut.get_readme()
    st.subheader("Background")
    st.write(excerpt)
    expander = st.expander("Read more...")
    expander.markdown(info)

    reproductive_cycles = st.sidebar.slider(
        "Reproductive cycles:",
        min_value=1,
        max_value=int(config.REPRODUCTIVE_CYCLES * 1.5),
        value=config.REPRODUCTIVE_CYCLES,
    )

    col1, col2 = st.sidebar.columns(2)

    with col1:

        initial_population = st.slider(
            "Initial population:",
            min_value=1,
            max_value=int(config.INITIAL_POPULATION * 1.5),
            value=config.INITIAL_POPULATION,
        )

        max_offspring = st.slider(
            "Maximum offspring:",
            min_value=1,
            max_value=int(config.MAX_OFFSPRING * 1.5),
            value=config.MAX_OFFSPRING,
        )

        max_partners = st.slider(
            "Maximum partners:",
            min_value=1,
            max_value=int(config.MAX_PARTNERS * 1.5),
            value=config.MAX_PARTNERS,
        )

    with col2:

        max_population = st.slider(
            "Maximum population:",
            min_value=initial_population,
            max_value=int(config.MAX_POPULATION * 1.5),
            value=config.MAX_POPULATION,
        )

        max_lifespan = st.slider(
            "Maximum lifespan:",
            min_value=1,
            max_value=int(config.MAX_LIFESPAN * 1.5),
            value=config.MAX_LIFESPAN,
        )

        crispr_females_percentage = st.slider(
            "CRISPR females (%):",
            min_value=0.01,
            max_value=5.0,
            value=config.CRISPR_FEMALES_PERCENTAGE * 100,
        )

    crispr_females_percentage /= 100

    # add progress bar and status text in sidebar
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.text("Simulation 0% complete")

    # if button clicked run the simulation
    if not st.sidebar.button(
        label="Run the Simulation", type="primary", use_container_width=True
    ):
        return

    # prepare the initial dataframe data (the first row)
    half_size = initial_population // 2
    crispr_females = int(crispr_females_percentage * half_size)
    healthy_females = half_size - crispr_females

    # prepare dataframe
    df = pd.DataFrame(
        [
            {
                "Healthy Males": half_size,
                "Healthy Females": healthy_females,
                "Sterile Males": 0,
                "CRISPR Females": crispr_females,
            }
        ],
        dtype=float,
    )

    df.index.name = "Reproductive Cycles"

    # replace the chart and table placeholders
    line_chart = chart_placeholder.line_chart(df, height=500, use_container_width=True)
    table = table_placeholder.dataframe(df, use_container_width=True)

    # build the population
    males, females = pop.create_population(
        initial_population, crispr_females_percentage, max_lifespan
    )

    # record the initial numbers
    population = len(males) + len(females)
    crispr_fems = [f for f in females if f.crispr]
    non_crispr_fems = [f for f in females if not f.crispr]
    total_pop, crispr, sterile = [population], [len(crispr_fems)], [0]
    non_sterile, non_crispr = [len(males)], [len(non_crispr_fems)]

    # go through the given number of cycles
    for i in range(reproductive_cycles):
        # produce offspring
        male_kids, female_kids = rep.reproduce(
            males, females, max_offspring, max_partners, max_lifespan
        )
        # add children to population
        males += male_kids
        females += female_kids

        # increase the age of males and females
        for m in males:
            m.age += 1
        for f in females:
            f.age += 1

        # remove the dead individuals
        males = [m for m in males if not m.dead]
        females = [f for f in females if not f.dead]

        # remove extra population if any to stay within the population limit
        if (extra := len(males) + len(females) - max_population) > 0:
            males = random.sample(males, k=len(males) - extra // 2)
            females = random.sample(females, k=len(females) - extra // 2)

        # refresh the population number
        population = len(males) + len(females)

        # introduce CRISPR edited gene in some of the females on every reproductive cycle
        count = int((initial_population // 2) * crispr_females_percentage)
        for f in females:
            if count <= 0 or f.crispr:
                continue
            f.crispr = True
            count -= 1

        # check sterile males and crispr females numbers
        crispr_fems = [f for f in females if f.crispr]
        non_crispr_fems = [f for f in females if not f.crispr]
        sterile_males = [m for m in males if m.sterile]
        non_sterile_males = [m for m in males if not m.sterile]

        # record (append) the population numbers for this cycle
        crispr.append(len(crispr_fems))  # CRISPR females
        non_crispr.append(len(non_crispr_fems))  # NON CRISPR females
        sterile.append(len(sterile_males))  # STERILE males
        non_sterile.append(len(non_sterile_males))  # NON STERILE males
        total_pop.append(population)  # total population

        df = pd.DataFrame(
            [
                {
                    "Healthy Males": non_sterile[-1],
                    "Healthy Females": non_crispr[-1],
                    "Sterile Males": sterile[-1],
                    "CRISPR Females": crispr[-1],
                }
            ],
            dtype=float,
        )

        time.sleep(0.05)
        line_chart.add_rows(df)
        table.add_rows(df)  # type: ignore

        # shuffle males and females
        random.shuffle(males)
        random.shuffle(females)

        percentage_complete = round(((i + 1) / reproductive_cycles) * 100)
        progress_bar.progress(percentage_complete)
        status_text.text(f"Simulation {percentage_complete}% complete")

    return dict(
        crispr=crispr,
        sterile=sterile,
        non_sterile=non_sterile,
        non_crispr=non_crispr,
        total_pop=total_pop,
    )
