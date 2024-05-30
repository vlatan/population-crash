import random

import config
import population as pop


def produce_kids(
    sexes: list[str], sterile: bool = False, crispr: bool = False
) -> pop.Population:
    """Produce number of children based on their sex and genes."""

    males = [pop.Male(age=0, sterile=sterile) for sex in sexes if sex == "male"]
    females = [pop.Female(age=0, crispr=crispr) for sex in sexes if sex == "female"]
    return males, females


def reproduce(
    males: pop.Males, females: pop.Females, max_offspring: int, max_male_partners: int
) -> pop.Population:
    """
    males, females: lists of male and female objects.
    --------------------------------------------------------
    Performs one cycle of mating which returns two lists of
    children (male and female objects with age = 0).
    """
    male_children: pop.Males = []
    female_children: pop.Females = []

    # loop through females
    for female in females:

        # randomly choose partners for this female
        partners_num = min(len(males), random.randrange(1, max_male_partners))
        partners = random.choices(males, k=partners_num)

        # if all partners are sterile this female will not produce offspring
        if all((partner.sterile for partner in partners)):
            continue

        # prepare a pool of random sexes for this female's children
        num_kids = random.randrange(1, max_offspring)
        sexes = [random.choice(("male", "female")) for _ in range(num_kids)]

        # produce kids based on whether the female parent has the CRISPR gene or not
        male_kids, female_kids = (
            produce_kids(sexes, sterile=True, crispr=True)
            if female.crispr
            else produce_kids(sexes)
        )

        # add this female's children to the pool of population's children
        male_children += male_kids
        female_children += female_kids

    return male_children, female_children
