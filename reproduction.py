import random
from population import *


def reproduce(males, females, offspring, lifespan):
    """ males, females: lists of male and female objects.
        offspring: max number of possible children per reproduction (int).
        --------------------------------------------------------
        Performs one cycle of mating which returns two lists of
        children (male and female objects). """

    # males and females ready for reproduction
    readyMales = [m for m in males if not m.ifDead()]
    readyFemales = [f for f in females if not f.ifDead()]
    smaller_pop = min(len(readyMales), len(readyFemales))
    newMales, newFemales = [], []

    # loop through the smaller population in size
    for i in range(smaller_pop):
        # if the male is not sterile
        if not readyMales[i].getSterile():
            # prepare a pool of children
            children = [random.choice(('male', 'female'))
                        for child in range(random.randrange(offspring + 1))]
            # if the female parent has the CRISPR gene
            # female children have CRISPR and male children are sterile
            if readyFemales[i].getCrispr():
                for s in children:
                    if s == 'male':
                        # new sterile male with random lifespan and age 0
                        newMales.append(
                            Male(lifespan=random.randrange(1, lifespan + 1), sterile=True))
                    if s == 'female':
                        # new CRISPR female with random lifespan and age 0
                        newFemales.append(
                            Female(lifespan=random.randrange(1, lifespan + 1), crispr=True))
            # if the female parent doesn't have the CRISPR gene
            # then children are normal
            elif not readyFemales[i].getCrispr():
                for s in children:
                    if s == 'male':
                        # new normal male with random lifespan and age 0
                        newMales.append(
                            Male(lifespan=random.randrange(1, lifespan + 1)))
                    if s == 'female':
                        # new normal female with random lifespan and age 0
                        newFemales.append(
                            Female(lifespan=random.randrange(1, lifespan + 1)))

    return newMales, newFemales
