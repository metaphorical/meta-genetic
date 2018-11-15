import random

# Hack for "Python as a framework" error on macos x
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt

from lib.city import City

import lib.ga_routines as GA

def geneticAlgorithm(population, popSize, fittestSize, mutationRate, generations):
    """
        Basic genetic algorithm implementation with building blocks assembled in ga_routines.py
        Outputs just calculated final distance
    """
    pop = GA.initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / GA.rankRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = GA.nextGeneration(pop, fittestSize, mutationRate)
    
    print("Final distance: " + str(1 / GA.rankRoutes(pop)[0][1]))
    bestRouteIndex = GA.rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute

def geneticAlgorithmPlot(population, popSize, fittestSize, mutationRate, generations):
    """
        Genetic Algorithm implementation that outputs calculation progress plot
    """
    pop = GA.initialPopulation(popSize, population)
    progress = []
    progress.append(1 / GA.rankRoutes(pop)[0][1])
    
    for i in range(0, generations):
        pop = GA.nextGeneration(pop, fittestSize, mutationRate)
        progress.append(1 / GA.rankRoutes(pop)[0][1])
    
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()


# Running it

cityList = []

for i in range(0,25):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

# geneticAlgorithm(population=cityList, popSize=100, fittestSize=20, mutationRate=0.01, generations=500)
geneticAlgorithmPlot(population=cityList, popSize=100, fittestSize=20, mutationRate=0.01, generations=500)

