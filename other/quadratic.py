#!/usr/bin/env python3
import math


def quadratic(a, b, c):
    x = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x


#print(quadratic(1,4,3))
