#!/usr/bin/env python3
def triangles():
    ls = [1]
    while 1:
        yield ls
        ls = [1] + list(map(sum, zip(ls[:-1], ls[1:]))) + [1]

o = triangles()
next(0)
next(0)
next(0)
