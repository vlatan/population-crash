import random
from dataclasses import dataclass

import config


@dataclass
class Individual:
    lifespan: int = random.randrange(1, config.MAX_LIFESPAN)
    age: int = random.randrange(lifespan)

    @property
    def dead(self) -> bool:
        """Checks whether the individual has expired."""
        return self.age >= self.lifespan


@dataclass
class Male(Individual):
    # Males are NOT sterile by default.
    sterile: bool = False


@dataclass
class Female(Individual):
    # Females do NOT carry edited gene by default.
    crispr: bool = False


type Males = list[Male]
type Females = list[Female]
type Population = tuple[list[Male], list[Female]]


def create_population(
    initial_population: int, crispr_female_percentage: float
) -> Population:
    """Returns: Tuple of two lists of male and female objects."""

    # males and females with random lifespan and age
    half_size = initial_population // 2
    males = [Male() for _ in range(half_size)]
    females = [Female() for _ in range(half_size)]
    females_num = len(females)

    # some number of random females have the CRISPR gene
    num_crispr_females = int(crispr_female_percentage * females_num)
    random_indices = random.sample(range(females_num - 1), k=num_crispr_females)
    for index in random_indices:
        females[index].crispr = True

    return males, females
