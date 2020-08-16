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

**Assumptions:**  
* An individual's lifespan is represented in female reproductive cycles rather than in years. 
So if a female has 3 reproductive cycles per year and the maximum lifespan 
of a member of that population is 4 years then the maximum lifespan is represented as 12 cycles.  
* Females and males form random pairs during every reproductive cycle. This is obviously not 
true for all species, thus this simulation is not applicable for all the species.

**Variables you can adjust for this simulation:**  
* **cycles** - number of reproductive cycles you want this simulation to run.  
* **initSize** - initial size of the population.  
* **offspring** - maximum number of children a pair can have.  
* **lifespan** - maximum number of female reproductive cycles.  
* **crisprFems** - number of females with CRISPR edited genes in the population.  
* **popLimit** - maximum size of the population (every population in the wild exists in some 
sort of equilibrium where its numbers are kept in check by predators, diseases, environment, etc).

~~~
results = simulate(cycles=2000,
                   initSize=1900,
                   offspring=12,
                   lifespan=4,
                   crisprFems=400,
                   popLimit=2000)
~~~

So, at every cycle males and females form random pairs to mate. They produce 
random number of male and female children. If a female parent carries CRISPR edited genes 
and the male parent is not sterile they will produce female children that carry 
CRISPR genes and sterile male children. Otherwise if the male parent is not sterile and 
the female parent has no CRISPR genes they will produce healthy offspring. However only a certain 
number of randomly chosen children per cycle actually survive (population limit minus 
current population size).

This simulation, as it is, shows that in order to crash a population you need 
a very high number of females with edited genes among the population. 
Although sometimes you can crash the population even with as little as 30% of 
the females being CRISPR edited, the higher that percentage the more likely it is 
the population to crash.
