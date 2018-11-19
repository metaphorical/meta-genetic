import random, operator

import pandas as pd
import numpy as np

from fitness import Fitness

def createRoute(cityList):
    """
    Creating random route around the cities

    :param cityList:
    :return route - randomized cityList:
    """
    route = random.sample(cityList, len(cityList))
    return route


def initialPopulation(popSize, cityList):
    """
    Setting up initial population of initial (random sample routes).

    We take set of randomly created routes around cities so we can work our way towards most optimal solution.

    :param popSize:
    :param cityList:
    :return population:
    """
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population


def rankRoutes(population):
    """
    Using individual fitness Class to rank routes
    (in this case only indicator of route fitness is it's length)

    :param population:
    :return ranked population:
    """
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)


def selection(popRanked, fittestSize):
    """
    We rank population and pick who survives the generation

    :param popRanked:
    :param fittestSize:
    :return selectionResult - List of positions (indices) of surviving individuals:
    """
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, fittestSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - fittestSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    """
    Picking up list of selected individuals using selection results.
    It is called mating pool, because these are individuals chosen to produce next generation.

    TODO: This should probably move to selection so it can output List of individuals
    :param population:
    :param selectionResults:
    :return matingPool:
    """
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    """
    We can't splice and crossover without making sure that each gene is included only ones.
    This is TS specific case since one city can be included in teh route exactly ones,
    and each city has to be included.

    :param parent1:
    :param parent2:
    :return breeding result (child, if you will):
    """
    childP1 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def breedPopulation(matingpool, fittestSize):
    """
    Create next genertion.

    :param matingpool:
    :param fittestSize:
    :return children:
    """
    children = []
    length = len(matingpool) - fittestSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,fittestSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

def mutate(individual, mutationRate):
    """
    Altho in some other cases this is also place of randomness,
    we have rule of routes containing all the cities and just ones, so we can swap... basically.

    This is done to make algorithm explore other local optimums (avoid convergence towards one)

    :param individual:
    :param mutationRate:
    :return mutated individual:
    """
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(currentGen, fittestSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, fittestSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, fittestSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration
