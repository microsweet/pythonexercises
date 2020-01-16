#!/usr/bin/env python3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print('hello ' + self.first_name.title() + ' ' +
              self.last_name.title())


class Privileges():
    def __init__(self):
        self.privileges = ['1', '2', '3']

    def show_privileges(self):
        for i in self.privileges:
            print(i)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin = Admin('Tony', 'Start')
admin.privileges.show_privileges()
