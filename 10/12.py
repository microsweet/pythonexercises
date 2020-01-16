#! /usr/bin/env python3
import json

filename = 'lovelynumber.json'


def get_lovely_num():
    try:
        with open(filename) as f_obj:
            lovely_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return lovely_num


def set_lovely_num():
    lovely_num = input('please input your lovely number: ')
    with open(filename, 'w') as f_obj:
        json.dump(lovely_num, f_obj)


def view():
    lovely_num = get_lovely_num()
    if lovely_num:
        print(lovely_num)
    else:
        set_lovely_num()


view()
