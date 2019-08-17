#!/usr/bin/env python3
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
if L2 == ['hello', 'world', 'apple']:
    print('true')
else:
    print('false')
