import random
from population import *


def reproduce(males, females, offspring, lifespan):
    """
    males, females: lists of male and female objects.
    offspring: max number of possible children per reproduction (int).
    --------------------------------------------------------
    Performs one cycle of mating which returns two lists of
    children (male and female objects).
    """
    # males and females ready for reproduction
    ready_males = [m for m in males if not m.dead]
    ready_females = [f for f in females if not f.dead]
    new_males, new_females = [], []

    # loop through the smaller population in size
    for male, female in zip(ready_males, ready_females):

        # if male sterile skip this pair
        if male.sterile:
            continue

        # prepare a pool of children
        children = [
            random.choice(("male", "female"))
            for child in range(random.randrange(offspring + 1))
        ]

        # if the female parent has the CRISPR gene
        # female children have CRISPR and male children are sterile
        if female.crispr:
            for s in children:
                if s == "male":
                    # new sterile male with random lifespan and age 0
                    new_males.append(
                        Male(lifespan=random.randrange(1, lifespan + 1), sterile=True)
                    )
                if s == "female":
                    # new CRISPR female with random lifespan and age 0
                    new_females.append(
                        Female(lifespan=random.randrange(1, lifespan + 1), crispr=True)
                    )
        # if the female parent doesn't have the CRISPR gene
        # then children are normal
        elif not female.crispr:
            for s in children:
                if s == "male":
                    # new normal male with random lifespan and age 0
                    new_males.append(Male(lifespan=random.randrange(1, lifespan + 1)))
                if s == "female":
                    # new normal female with random lifespan and age 0
                    new_females.append(
                        Female(lifespan=random.randrange(1, lifespan + 1))
                    )

    return new_males, new_females
