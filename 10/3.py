#! /usr/bin/env python3

filename = 'guest.txt'
name = input('请输入用户名：')
with open(filename, 'a') as file_object:
    file_object.write(name + '\n')
