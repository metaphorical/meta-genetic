# Genetic algorythm

Playing with genetic algorythms.

## Short theory

Genetic Algorithm is the one of the simplest types of Evolutionary Algorithms. 

It is based on Charles Darwin's theory of natural evolution, also known as "survival of the fittest". It is also random based.

It is yet another technical concept learning from nature, and as many others we see around us, it has high abstraction potential - if you approach problem with good GA prep, you can solve lots of stuff using this natural approach.

### Basic concepts and processes (components)

#### Genes
Set of parameters characterizing the individual.

#### Individual (aka Chromosome or solution)
Combination of parameters - string of genes. It is usually one of the solutions to a problem we are trying to solve

#### Population
Set of individuals. This is, in abstract sense, pool of solutions to a problem we are solvinge.

#### Parents
Individuals selected for the reproduction - this selection is actually what is **survival of the fittest** in essence. The parents that are chosen to mate and produce next generation are **fittest individuals**. Fitness is determined by **Fitness function**

#### Fitness function
Fitness function provides fitness score that is used to rank individuals within population.

#### Selection > Mating pool
Selection proces produces number of individuals from the population (elite) to be included in the "mating pool". Mating pool produces next generation (population) of individuals.

#### Crossover

This is the place of randomness. It is also significant point in algorithm. 

Crossover point between two parents is chosen at random (within the parents) and genes are exchanged between them untill they reach crossover point. **This is how offsprings are created**.

Newly created offsprings are added to the populaton.

#### Mutation

Mutation is randomization concept that occurs with low probability. It is usual that mutation is jsut fliping the genes or doing some other shallow change.

Main purpose of the mutation is avoiding premature convergence.

#### Convergence (Termination)

End of the algorithm occurs when it does not produce offsprings that are significately different then last generation (evolution is done)
