#! /usr/bin/env python3
import json

filename='lovelynumber.txt'
with open(filename) as f_obj:
    number = json.load(f_obj)
    print(number)
