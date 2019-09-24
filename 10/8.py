#! /usr/bin/env python3
fileCat = 'cat.txt'
fileDog = 'dog.txt'

def printName(names):
    for name in names:
        print(name.rstrip())

try:
    with open(fileCat) as file_object:
        catNames = file_object.readlines()
    with open(fileDog) as file_object:
        dogNames = file_object.readlines()
except FileNotFound:
    print('文件不存在')
else:
    printName(catNames)
    printName(dogNames)

