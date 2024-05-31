import time
import random
import pandas as pd
import streamlit as st

import config
import population as pop
import reproduction as rep


def simulate() -> dict[str, config.Vector] | None:
    """
    Records the relevant numbers after every cycle.
    Returns the numbers for each population category in a dict.
    """

    st.subheader("Simulation Chart")

    st.write(
        """
        Press **the button in the sidebar** to run the simulation. The chart will re-render
        showing the updated population numbers: healthy males and females, sterile males 
        and females that cary a CRISPR edited gene. [Read more ↓](/#gene-drive-population-crash-simulation)
        """
    )

    # get ready made dataframe from CSV file just for the initial page load display
    placeholder_df = read_simulation_csv()

    chart_placeholder = st.empty()
    chart_placeholder.line_chart(placeholder_df, height=500, use_container_width=True)

    st.subheader("Simulation Table")
    st.write(
        """
        When you run the simulation the table will "grow" downwards, new rows will be added at each life cycle, 
        showing how the numbers of the population behave in each life cycle.
        """
    )

    table_placeholder = st.empty()
    table_placeholder.dataframe(placeholder_df, use_container_width=True)

    life_cycles = st.sidebar.slider(
        "Life cycles:",
        min_value=1,
        max_value=int(config.LIFE_CYCLES * 1.5),
        value=config.LIFE_CYCLES,
    )

    col1, col2 = st.sidebar.columns(2)

    initial_population = col1.slider(
        "Initial population:",
        min_value=1,
        max_value=int(config.INITIAL_POPULATION * 1.5),
        value=config.INITIAL_POPULATION,
    )

    max_population = col2.slider(
        "Maximum population:",
        min_value=initial_population,
        max_value=int(config.MAX_POPULATION * 1.5),
        value=config.MAX_POPULATION,
    )

    max_offspring = col1.slider(
        "Maximum offspring:",
        min_value=1,
        max_value=int(config.MAX_OFFSPRING * 1.5),
        value=config.MAX_OFFSPRING,
    )

    max_lifespan = col2.slider(
        "Maximum lifespan:",
        min_value=1,
        max_value=int(config.MAX_LIFESPAN * 1.5),
        value=config.MAX_LIFESPAN,
    )

    max_male_partners = col1.slider(
        "Maximum partners:",
        min_value=1,
        max_value=int(config.MAX_MALE_PARTNERS * 1.5),
        value=config.MAX_MALE_PARTNERS,
    )

    crispr_females_percentage = col2.slider(
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

    # calculate the initial dataframe numbers
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

    df.index.name = "Life Cycles"

    # replace chart and table with empty ones
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
    for i in range(life_cycles):
        # produce offspring
        male_kids, female_kids = rep.reproduce(
            males, females, max_offspring, max_male_partners, max_lifespan
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

        # introduce CRISPR gene in some of the females on every life cycle
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

        percentage_complete = round(((i + 1) / life_cycles) * 100)
        progress_bar.progress(percentage_complete)
        status_text.text(f"Simulation {percentage_complete}% complete")

    return dict(
        crispr=crispr,
        sterile=sterile,
        non_sterile=non_sterile,
        non_crispr=non_crispr,
        total_pop=total_pop,
    )


@st.cache_data(show_spinner=False)
def read_simulation_csv() -> pd.DataFrame:
    return pd.read_csv("simulation.csv", index_col="Life Cycles")
