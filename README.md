# Gene Drive Population Crash Simulation

**CRISPR** technology is a powerful tool for editing genomes.
It allows scientists to easily alter DNA sequences and modify genes.
Even more so it can be used to pass those altered genes to the next
generation (**Gene Drive**) with 100% certainty and to all offspring instead of
to just 50%.

By doing so, with gene drive you can even crash a population if you
successfully propagate certain genes through that population. Scientists are
already experimenting with mosquitoes and rats. For example they can eradicate
malaria if they crash the population of mosquitoes that carry and spread malaria.

In this simulation, we can arbitrarily introduce number of females into the population
with CRISPR edited genes which assure that their male offspring are sterile
and their female offspring are carrying those same CRISPR edited genes.
By doing this it is likely that sterile males and CRISPR females will propagate and
spread through the population and if they reach a critical number the population may
even crash.

![Population Crash](/crash.png?raw=true "Population Crash")

**Assumptions:**
* An individual's lifespan is represented in female reproductive cycles rather than in years.
So if a female has 3 reproductive cycles per year and the maximum lifespan
of a member of that population is 4 years then the maximum lifespan is represented as 12 cycles.
* Females can have multiple partners as is the case in many of the species to ensure reproduction. Only if all of her partners are sterile only then the female will not have offspring during that cycle.

**Constants you can adjust for this simulation:**
* **LIFE_CYCLES** - number of reproductive cycles you want this simulation to run.
* **INITIAL_POPULATION** - initial size of the population.
* **MAX_OFFSPRING** - maximum number of children female can have per cycle.
* **MAX_LIFESPAN** - maximum lifespan of the species (number of female reproductive cycles).
* **MAX_MALE_PARTNERS** - maximum number of partners female can have per cycle.
* **CRISPR_FEMALES_PERCENTAGE** - percentage of females with CRISPR edited gene.
* **MAX_POPULATION** - population limit which external forces (predators, diseases, etc.) keep in check.

So, at every cycle a female mates with a number of random partners. The female gives birth to a random number of male and female children. If a female parent carries the CRISPR edited gene
and at least one of her partners was not sterile they will produce female children that carry the
CRISPR gene and male children that are sterile. Otherwise if the female parent has no CRISPR gene they will produce healthy offspring.

This simulation, as it is, shows that in order to crash a population, in every cycle you need to introduce as little as 1.6% females of the initial female population with edited genes.

You must first assure though that the constants are adjusted as such that the population will not crush by itself due to death rate being higher than the birth rate.

## License

[![License: MIT](https://img.shields.io/github/license/vlatan/population-crash?label=License)](/LICENSE "License: MIT")