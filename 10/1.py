#! /usr/bin/env python3
filename = 'learning_python.txt'
with open(filename) as file_object:
    print1 = file_object.read()
    print(print1)

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
