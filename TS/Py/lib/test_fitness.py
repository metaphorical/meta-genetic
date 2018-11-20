import unittest

from city import City
from fitness import Fitness

test_route = [City(x=0, y=0), City(x=4, y=0), City(x=0, y=3)]

class TestFitness(unittest.TestCase):
    def test_route_distance(self):
        fitness = Fitness(test_route)
        # it is classic 3-4-5 orthogonal triangle
        self.assertEqual(12, fitness.routeDistance())

    def test_route_fitness(self):
        fitness = Fitness(test_route)

        self.assertEqual(1 / float(12), fitness.routeFitness())
