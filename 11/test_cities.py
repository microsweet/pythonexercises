#! /usr/bin/env python3
import unittest
from city_functions import country_city

class test_city_functions(unittest.TestCase):
#    def test_city_country(self):
#        citys = country_city('santaigo', 'chile')
#        self.assertEqual(citys, 'Santaigo Chile')

    def test_city_country_population(self):
        city_country_pop = country_city('santaigo', 'chile', 5000000)
        self.assertEqual(city_country_pop, 'Chile, Santaigo - population 5000000')

unittest.main()
