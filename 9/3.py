#!/usr/bin/env python3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print('hello ' + self.first_name.title() + ' ' + self.last_name.title())

tony = User('Tony', 'Start')
peter = User('Peter', 'Park')

tony.describe_user()
tony.greet_user()
peter.describe_user()
peter.greet_user()
