import random

CYCLES = 400
INITIAL_POPULATION = 1900
MAX_OFFSPRING = 13
MAX_LIFESPAN = 5
MAX_MALE_PARTNERS = 4
CRISPR_FEMALES = 500
POPULATION_LIMIT = 2000


class Individual:
    def __init__(self, age=None):
        """
        The lifespan determines the maximum mating cycles for this individual.
        The age is elapsed mating cycles so far.
        """
        self.lifespan = random.randrange(1, MAX_LIFESPAN)
        self.age = random.randrange(self.lifespan) if age is None else age

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
    def __init__(self, sterile=False):
        """Males are NOT sterile by default."""
        super().__init__()
        self.sterile = sterile

    def __str__(self):
        return f"Male -> sterile = {str(self.sterile)}, {super().__str__()}"


class Female(Individual):
    def __init__(self, crispr=False):
        """Females do NOT carry CRISPR gene by default."""
        super().__init__()
        self.crispr = crispr

    def __str__(self):
        return f"Female -> CRISPR = {str(self.crispr)}, {super().__str__()}"


def create_population():
    """
    size: desired number of individuals in the population (int).
    lifespan: max number of mating cycles of an individual (int).
    crisprFemales: number of initial females with CRIPSR gene (int).
    -------------------------------------------------
    Returns: two lists of male and female objects.
    """

    # males and females with random lifespan and age
    half_size = INITIAL_POPULATION // 2
    males = [Male() for _ in range(half_size)]
    females = [Female() for _ in range(half_size)]

    # some number of random females have the CRISPR gene
    for _ in range(CRISPR_FEMALES):
        random_index = random.randint(0, len(females) - 1)
        females[random_index].crispr = True

    return males, females
