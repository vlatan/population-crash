import random


class Individual:
    def __init__(self, lifespan, age=0):
        """
        The age is expressed in mating cycles.
        The lifespan determines the maximum mating cycles.
        """
        self.lifespan = lifespan
        self.age = age

    def get_age(self):
        return self.age

    def increase_age(self):
        self.age += 1

    def get_lifespan(self):
        return self.lifespan

    def if_dead(self):
        """Checks whether the individual has expired"""
        return self.get_age() > self.get_lifespan()

    def __str__(self):
        return (
            "age = "
            + str(self.get_age())
            + ", lifespan = "
            + str(self.get_lifespan())
            + ", dead = "
            + str(self.if_dead())
        )


class Male(Individual):
    def __init__(self, lifespan, age=0, sterile=False):
        """Males are NOT sterile by default"""
        Individual.__init__(self, lifespan, age)
        self.sterile = sterile

    def get_sterile(self):
        return self.sterile

    def __str__(self):
        return (
            "<Male -> sterile = "
            + str(self.get_sterile())
            + ", "
            + Individual.__str__(self)
            + ">"
        )


class Female(Individual):
    def __init__(self, lifespan, age=0, crispr=False):
        """Females do NOT carry CRISPR gene by default"""
        Individual.__init__(self, lifespan, age)
        self.crispr = crispr

    def get_crispr(self):
        return self.crispr

    def __str__(self):
        return (
            "<Female -> CRISPR = "
            + str(self.get_crispr())
            + ", "
            + Individual.__str__(self)
            + ">"
        )


def buildPopulation(size, lifespan, crisprFemales):
    """size: desired number of individuals in the population (int).
    lifespan: max number of mating cycles of an individual (int).
    crisprFemales: number of initial females with CRIPSR gene (int).
    -------------------------------------------------
    Returns: two lists of male and female objects."""

    # males with random lifespan and age
    males = [
        Male(
            lifespan=random.randrange(1, lifespan + 1),
            age=random.randrange(1, lifespan + 1),
        )
        for i in range(size // 2)
    ]
    # females with random lifespan and age
    females = [
        Female(
            lifespan=random.randrange(1, lifespan + 1),
            age=random.randrange(1, lifespan + 1),
        )
        for i in range(size - len(males) - crisprFemales)
    ]
    # add CRISPR females in population
    females += [
        Female(
            lifespan=random.randrange(1, lifespan + 1),
            age=random.randrange(1, lifespan + 1),
            crispr=True,
        )
        for i in range(crisprFemales)
    ]
    # shuffle females so the CRISPR females
    # are not at the end of the list.
    random.shuffle(females)
    return males, females
