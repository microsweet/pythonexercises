#!/usr/bin/env python3
import user

class Privileges():
    def __init__(self):
        self.privileges = ['1', '2', '3']

    def show_privileges(self):
        for i in self.privileges:
            print(i)

class Admin(user.User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

