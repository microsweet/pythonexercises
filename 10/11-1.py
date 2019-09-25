#! /usr/bin/env python3
import json

filename = 'lovelynumber.txt'
with open(filename, 'w') as f_obj:
    lovelyNum = input('请输入喜欢的数字')
    json.dump(lovelyNum, f_obj)
