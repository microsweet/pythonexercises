#!/usr/bin/env python3
def trim(s):
    if s[:1]==' ':
        return trim(s[1:])
    elif s[-1:]==' ':
        return trim(s[:-1])
    else:
        return s

def test():
    if trim('hello  ') != 'hello':
        print('error')
    elif trim('  hello') != 'hello':
        print('error')
    elif trim('  hello  ') != 'hello':
        print('error')
    elif trim('  hello world  ') != 'hello world':
        print('error')
    elif trim('') != '':
        print('error')
    elif trim('    ') != '':
        print('error')
    else:
        print('success')

test()

