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

    # add progress bar and status text in sidebar
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.text("Simulation 0% complete")

    # calculate the initial dataframe numbers
    half_size = config.INITIAL_POPULATION // 2
    crispr_females = int(config.CRISPR_FEMALES_PERCENTAGE * half_size)
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

    st.subheader("Simulation Chart")

    st.write(
        """
        When you run the simulation the chart will "grow" to the right showing the updated population numbers - 
        healthy males and females, sterile males and "CRISPR" females which cary a special modified gene
        that makes their male offspring sterile and passes the same modified gene to their female offspring.
        """
    )
    chart = st.line_chart(df, height=500, use_container_width=True)

    st.subheader("Simulation Table")
    st.write(
        """
        When you run the simulation the table will "grow" downwards, new rows will be added at each life cycle, 
        showing how the numbers of the population behave in each life cycle.
        """
    )

    table = st.dataframe(df, use_container_width=True)

    # if button clicked run the simulation
    if not st.sidebar.button("Run Simulation"):
        return

    # build the population
    males, females = pop.create_population()

    # record the initial numbers
    population = len(males) + len(females)
    crispr_fems = [f for f in females if f.crispr]
    non_crispr_fems = [f for f in females if not f.crispr]
    total_pop, crispr, sterile = [population], [len(crispr_fems)], [0]
    non_sterile, non_crispr = [len(males)], [len(non_crispr_fems)]

    # go through the given number of cycles
    for i in range(config.LIFE_CYCLES):
        # produce offspring
        male_kids, female_kids = rep.reproduce(males, females)
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
        if (extra := len(males) + len(females) - config.MAX_POPULATION) > 0:
            males = random.sample(males, k=len(males) - extra // 2)
            females = random.sample(females, k=len(females) - extra // 2)

        # refresh the population number
        population = len(males) + len(females)

        # introduce CRISPR gene in some of the females on every life cycle
        count = int((config.INITIAL_POPULATION // 2) * config.CRISPR_FEMALES_PERCENTAGE)
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
        table.add_rows(df)  # type: ignore
        chart.add_rows(df)

        # shuffle males and females
        random.shuffle(males)
        random.shuffle(females)

        percentage_complete = round(((i + 1) / config.LIFE_CYCLES) * 100)
        progress_bar.progress(percentage_complete)
        status_text.text(f"Simulation {percentage_complete}% complete")

    return dict(
        crispr=crispr,
        sterile=sterile,
        non_sterile=non_sterile,
        non_crispr=non_crispr,
        total_pop=total_pop,
    )
