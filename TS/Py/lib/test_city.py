import unittest

from city import City


class TestCity(unittest.TestCase):
    def test_city_distance(self):
        zero_city = City(0,0)
        test_city = City(3,4)
        self.assertEqual(5, zero_city.distance(test_city))
