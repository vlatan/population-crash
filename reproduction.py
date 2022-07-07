import random
from population import *


def produce_kids(sexes, sterile=False, crispr=False):
    """Produce number of children based on their sex and genes."""
    males = [Male(age=0, sterile=sterile) for sex in sexes if sex == "male"]
    females = [Female(age=0, crispr=crispr) for sex in sexes if sex == "female"]
    return males, females


def reproduce(males, females):
    """
    males, females: lists of male and female objects.
    --------------------------------------------------------
    Performs one cycle of mating which returns two lists of
    children (male and female objects with age = 0).
    """
    male_children, female_children = [], []

    # loop through females
    for female in females:
        # randomly choose partners for this female
        partners = random.choices(males, k=random.randrange(1, MAX_MALE_PARTNERS))
        # if all partners are sterile this female will not produce offspring
        if all((partner.sterile for partner in partners)):
            continue

        # prepare a pool of random sexes for this female's children
        num_kids = random.randrange(1, MAX_OFFSPRING)
        sexes = [random.choice(("male", "female")) for _ in range(num_kids)]

        # if the female parent doesn't have the CRISPR gene
        male_kids, female_kids = produce_kids(sexes)
        # if the female parent has the CRISPR gene
        if female.crispr:
            male_kids, female_kids = produce_kids(sexes, sterile=True, crispr=True)

        # add children to the pool of children
        male_children += male_kids
        female_children += female_kids

    return male_children, female_children
