#!/usr/bin/env python3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print('hello ' + self.first_name.title() + ' ' + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

tony = User('Tony', 'Start')
tony.increment_login_attempts()
tony.increment_login_attempts()
tony.increment_login_attempts()
tony.increment_login_attempts()
print(tony.login_attempts)
tony.reset_login_attempts()
print(tony.login_attempts)
