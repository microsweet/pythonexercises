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


restaurant = Restaurant('kfc', 'quickly')
restaurant.describe_restaurant()
restaurant.open_restaurant()
