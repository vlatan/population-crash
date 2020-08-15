import random
from population import *
from reproduction import *


def simulate(cycles, initSize, offspring, lifespan, crisprFems, popLimit):
    """ cycles: the number of cycles this simulation will run.
        initSize: the initial size of the population.
        offspring: max number of possible children per reproduction.
        lifespan: maximum lifespan of an individual.
        crisprFems: the initial number of CRISPR females in the population.
        popLimit: the maximum size this population can get.
        ---------------------------------------------------
        Records the relevant numbers after every cycle.
        Returns the numbers for each population category in a dict. """

    # build the population
    males, females = buildPopulation(initSize, lifespan, crisprFems)

    # record the initial numbers
    population = len(males) + len(females)
    totalPop, crispr, sterile = [population], [crisprFems], [0]
    nonSterile, nonCrispr = [0], [len(females) - crisprFems]

    # go through the given number of cycles
    for cycle in range(cycles):
        # refresh the population numbers
        population = len(males) + len(females)
        # if population hasn't reached the limit
        if population < popLimit:
            # produce offspring
            maleKids, femaleKids = reproduce(
                males, females, offspring, lifespan)
            # select random sample from the offspring in this cycle
            numChildren = min((popLimit - population) //
                              2, len(maleKids), len(femaleKids))
            # add them to the population
            males += random.sample(maleKids, numChildren)
            random.shuffle(femaleKids)
            females += random.sample(femaleKids, numChildren)
        # increase age the end of every cycle
        for m in males:
            m.increaseAge()
        for f in females:
            f.increaseAge()

        # remove the dead individuals
        males = [m for m in males if not m.ifDead()]
        females = [f for f in females if not f.ifDead()]
        # check how many CRISPR females are there
        crisprF = [f for f in females if f.getCrispr()]
        # check how many sterile males are there
        sterileM = [m for m in males if m.getSterile()]
        # check how many healthy females are there
        nonCrisprF = [f for f in females if not f.getCrispr()]
        # check how many healthy males are there
        nonSterileM = [m for m in males if not m.getSterile()]

        # shuffle males and females
        random.shuffle(males)
        random.shuffle(females)

        # record (append) the population numbers for this cycle
        crispr.append(len(crisprF))            # CRISPR females
        sterile.append(len(sterileM))          # sterile males
        nonSterile.append(len(nonSterileM))    # non STERILE males
        nonCrispr.append(len(nonCrisprF))      # non CRISPR females
        totalPop.append(population)            # total population

    return dict(crispr=crispr,
                sterile=sterile,
                nonSterile=nonSterile,
                nonCrispr=nonCrispr,
                totalPop=totalPop)
