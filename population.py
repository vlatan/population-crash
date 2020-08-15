import random


class Individual(object):
    def __init__(self, lifespan, age=0):
        """ The age is expressed in mating cycles.
            The lifespan determines the maximum mating cycles. """
        self.lifespan = lifespan
        self.age = age

    def getAge(self):
        return self.age

    def increaseAge(self):
        self.age += 1

    def getLifespan(self):
        return self.lifespan

    def ifDead(self):
        """ Checks whether the individual has expired """
        return self.getAge() > self.getLifespan()

    def __str__(self):
        return 'age = ' + str(self.getAge()) + \
               ', lifespan = ' + str(self.getLifespan()) + \
               ', dead = ' + str(self.ifDead())


class Male(Individual):
    def __init__(self, lifespan, age=0, sterile=False):
        """ Males are NOT sterile by default """
        Individual.__init__(self, lifespan, age)
        self.sterile = sterile

    def getSterile(self):
        return self.sterile

    def __str__(self):
        return '<Male -> sterile = ' + str(self.getSterile()) + \
               ', ' + Individual.__str__(self) + '>'


class Female(Individual):
    def __init__(self, lifespan, age=0, crispr=False):
        """ Females do NOT carry CRISPR gene by default """
        Individual.__init__(self, lifespan, age)
        self.crispr = crispr

    def getCrispr(self):
        return self.crispr

    def __str__(self):
        return '<Female -> CRISPR = ' + str(self.getCrispr()) + \
               ', ' + Individual.__str__(self) + '>'


def buildPopulation(size, lifespan, crisprFemales):
    """ size: desired number of individuals in the population (int).
        lifespan: max number of mating cycles of an individual (int).
        crisprFemales: number of initial females with CRIPSR gene (int).
        -------------------------------------------------
        Returns: two lists of male and female objects. """

    # males with random lifespan and age
    males = [Male(lifespan=random.randrange(1, lifespan + 1),
                  age=random.randrange(1, lifespan + 1))
             for i in range(size // 2)]
    # females with random lifespan and age
    females = [Female(lifespan=random.randrange(1, lifespan + 1),
                      age=random.randrange(1, lifespan + 1))
               for i in range(size - len(males) - crisprFemales)]
    # add CRISPR females in population
    females += [Female(lifespan=random.randrange(1, lifespan + 1),
                       age=random.randrange(1, lifespan + 1), crispr=True)
                for i in range(crisprFemales)]
    # shuffle females so the CRISPR females
    # are not at the end of the list.
    random.shuffle(females)
    return males, females
