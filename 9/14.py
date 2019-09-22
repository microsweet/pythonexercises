#! /usr/bin/env python3
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print('side' + str(self.sides) + ' ' + str(randint(1, self.sides)))

side6 = Die()
side7 = Die(20)
x = 0
while x<10:
    side6.roll_die()
    side7.roll_die()
    x += 1
