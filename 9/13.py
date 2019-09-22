#! /usr/bin/env python3
from collections import OrderedDict

language = OrderedDict()

language['1'] = 'python'
language['2'] = 'java'
language['3'] = 'c'

for a, b in language.items():
    print(a + ' ' + b)



