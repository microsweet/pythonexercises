#!/usr/bin/env python3
def findMinAndMax(L):
    max = None
    min = None
    for i in L:
        if max == None or max > i:
            max = i
        if min == None or min < i:
            min = i
    return (max, min)


def test():
    if findMinAndMax([]) != (None, None):
        print('fail')
    elif findMinAndMax([7]) != (7, 7):
        print('fail')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('fail')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('fail')
    else:
        print('success')


test()
