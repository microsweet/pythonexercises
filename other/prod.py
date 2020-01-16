from functools import reduce


def prod(L):
    return reduce(dd, L)


def dd(x, y):
    return x * y


print('3*5*7*9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('success')
else:
    print('error')
