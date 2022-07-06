import random


class Individual:
    def __init__(self, lifespan, age=0):
        """
        The age is expressed in mating cycles.
        The lifespan determines the maximum mating cycles.
        """
        self.lifespan = lifespan
        self.age = age

    @property
    def dead(self):
        """Checks whether the individual has expired."""
        return self.age > self.lifespan

    def __str__(self):
        return (
            f"age = {str(self.age)}, "
            f"lifespan = {str(self.lifespan)}, "
            f"dead = {str(self.dead)}"
        )


class Male(Individual):
    def __init__(self, lifespan, age=0, sterile=False):
        """Males are NOT sterile by default."""
        super().__init__(lifespan, age)
        self.sterile = sterile

    def __str__(self):
        return f"Male -> sterile = {str(self.sterile)}, {super().__str__()}"


class Female(Individual):
    def __init__(self, lifespan, age=0, crispr=False):
        """Females do NOT carry CRISPR gene by default."""
        super().__init__(lifespan, age)
        self.crispr = crispr

    def __str__(self):
        return f"Female -> CRISPR = {str(self.crispr)}, {super().__str__()}"


def create_population(size, lifespan, crispr_females):
    """
    size: desired number of individuals in the population (int).
    lifespan: max number of mating cycles of an individual (int).
    crisprFemales: number of initial females with CRIPSR gene (int).
    -------------------------------------------------
    Returns: two lists of male and female objects.
    """

    def span_age(lifespan):
        """Returns tuple of random lifespan and age."""
        span = random.randrange(1, lifespan + 1)
        age = random.randrange(1, lifespan + 1)
        return span, age

    # males and females with random lifespan and age
    males, females = [], []
    for _ in range(size // 2):
        span, age = span_age(lifespan)
        males.append(Male(lifespan=span, age=age))

        span, age = span_age(lifespan)
        females.append(Female(lifespan=span, age=age))

    # some random females have the CRISPR gene
    for _ in range(crispr_females):
        random_index = random.randint(0, len(females) - 1)
        females[random_index].crispr = True

    return males, females
