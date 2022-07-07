import random
from population import *
from reproduction import *


def simulate():
    """
    Records the relevant numbers after every cycle.
    Returns the numbers for each population category in a dict.
    """
    # build the population
    males, females = create_population()

    # record the initial numbers
    population = len(males) + len(females)
    total_pop, crispr, sterile = [population], [CRISPR_FEMALES], [0]
    non_sterile, non_crispr = [0], [len(females) - CRISPR_FEMALES]

    # go through the given number of cycles
    for _ in range(CYCLES):
        # if population hasn't reached the limit
        if population < POPULATION_LIMIT:
            # produce offspring
            male_kids, female_kids = reproduce(males, females)
            # add surviving children to fit the population
            rest = (POPULATION_LIMIT - population) // 2
            num_kids = min(rest, len(male_kids), len(female_kids))
            males += random.sample(male_kids, num_kids)
            females += random.sample(female_kids, num_kids)

        # increase the age of the individuals
        for m in males:
            m.age += 1
        for f in females:
            f.age += 1

        # remove the dead individuals
        males = [m for m in males if not m.dead]
        females = [f for f in females if not f.dead]
        # refresh the population number
        population = len(males) + len(females)

        crispr_fems = [f for f in females if f.crispr]
        sterile_males = [m for m in males if m.sterile]

        # record (append) the population numbers for this cycle
        crispr.append(len(crispr_fems))  # CRISPR females
        non_crispr.append(len(females) - len(crispr_fems))  # NON CRISPR females
        sterile.append(len(sterile_males))  # STERILE males
        non_sterile.append(len(males) - len(sterile_males))  # NON STERILE males
        total_pop.append(population)  # total population

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
