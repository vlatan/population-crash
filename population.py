import random


class Individual:
    def __init__(self, lifespan: int, age: int):
        self.lifespan = lifespan
        self.age = age

        if self.age > self.lifespan:
            raise ValueError("Age cannot be bigger than lifespan.")

    @property
    def dead(self) -> bool:
        """Checks whether the individual has expired."""
        return self.age >= self.lifespan


class Male(Individual):
    def __init__(self, lifespan: int, age: int, sterile: bool = False):
        # Males are NOT sterile by default.
        super().__init__(lifespan, age)
        self.sterile = sterile


class Female(Individual):
    def __init__(self, lifespan: int, age: int, crispr: bool = False):
        # Males are NOT sterile by default.
        super().__init__(lifespan, age)
        self.crispr = crispr


type Males = list[Male]
type Females = list[Female]
type Population = tuple[list[Male], list[Female]]


def create_population(
    initial_population: int, crispr_female_percentage: float, max_lifespan: int
) -> Population:
    """Returns: Tuple of two lists of male and female objects."""

    # males and females with random lifespan and age
    half_size = initial_population // 2
    males, females = [], []

    for _ in range(half_size):
        lifespan = random.randrange(1, max_lifespan)
        age = random.randrange(lifespan)
        males.append(Male(lifespan=lifespan, age=age))

        lifespan = random.randrange(1, max_lifespan)
        age = random.randrange(lifespan)
        females.append(Female(lifespan=lifespan, age=age))

    females_num = len(females)

    # some number of random females have the CRISPR gene
    num_crispr_females = int(crispr_female_percentage * females_num)
    random_indices = random.sample(range(females_num - 1), k=num_crispr_females)
    for index in random_indices:
        females[index].crispr = True

    return males, females
