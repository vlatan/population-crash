import random
from dataclasses import dataclass

CYCLES = 100
INITIAL_POPULATION = 1000
MAX_OFFSPRING = 4
MAX_LIFESPAN = 2
MAX_MALE_PARTNERS = 4
CRISPR_FEMALES = 0.004


@dataclass
class Individual:
    lifespan: int = random.randrange(1, MAX_LIFESPAN)
    age: int = random.randrange(lifespan)

    @property
    def dead(self):
        """Checks whether the individual has expired."""
        return self.age > self.lifespan


@dataclass
class Male(Individual):
    # Males are NOT sterile by default.
    sterile: bool = False


@dataclass
class Female(Individual):
    # Females do NOT carry edited gene by default.
    crispr: bool = False


def create_population():
    """Returns: Tuple of two lists of male and female objects."""

    # males and females with random lifespan and age
    half_size = INITIAL_POPULATION // 2
    males = [Male() for _ in range(half_size)]
    females = [Female() for _ in range(half_size)]
    females_num = len(females)

    # some number of random females have the CRISPR gene
    for _ in range(int(CRISPR_FEMALES * females_num)):
        random_index = random.randint(0, females_num - 1)
        females[random_index].crispr = True

    return males, females
