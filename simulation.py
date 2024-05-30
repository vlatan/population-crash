import time
import random
import population as pop
import reproduction as rep
import config
import streamlit as st
import pandas as pd


def simulate() -> dict[str, config.Vector] | None:
    """
    Records the relevant numbers after every cycle.
    Returns the numbers for each population category in a dict.
    """
    # build the population
    males, females = pop.create_population()

    # record the initial numbers
    population = len(males) + len(females)
    crispr_fems = [f for f in females if f.crispr]
    non_crispr_fems = [f for f in females if not f.crispr]
    total_pop, crispr, sterile = [population], [len(crispr_fems)], [0]
    non_sterile, non_crispr = [len(males)], [len(non_crispr_fems)]

    df = pd.DataFrame(
        [
            {
                "Healthy Males": non_sterile[0],
                "Healthy Females": non_crispr[0],
                "Sterile Males": sterile[0],
                "CRISPR Females": crispr[0],
            }
        ],
        dtype=float,
    )

    chart = st.line_chart(df, height=500, use_container_width=True)
    table = st.dataframe(df)

    # go through the given number of cycles
    for _ in range(config.CYCLES):
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
        if (extra := len(males) + len(females) - config.POPULATION_LIMIT) > 0:
            males = random.sample(males, k=len(males) - extra // 2)
            females = random.sample(females, k=len(females) - extra // 2)

        # refresh the population number
        population = len(males) + len(females)

        # introduce CRISPR gene in some of the females
        count = int((config.INITIAL_POPULATION // 2) * config.CRISPR_FEMALES)
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

    return dict(
        crispr=crispr,
        sterile=sterile,
        non_sterile=non_sterile,
        non_crispr=non_crispr,
        total_pop=total_pop,
    )
