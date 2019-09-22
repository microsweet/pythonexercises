#!/usr/bin/env python3
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('restaurant is open')

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, may_served):
        self.number_served = self.number_served
        self.may_served = may_served

restaurant = Restaurant('kfc', 'quickly')
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(100)

