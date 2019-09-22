#!/usr/bin/env python3
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('restaurant is open')

class Icecreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'raspberry', 'apple']

    def showFlavors(self):
        for i in self.flavors:
            print(i)

icecreamstand = Icecreamstand('Haagen-Dazs', 'quickly')
icecreamstand.showFlavors()

