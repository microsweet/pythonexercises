#! /usr/bin/env python3
filename = 'reason_like_program.txt'
with open(filename, 'a') as file_object:
    flag = True
    while flag:
        reason = input('Why are you like program?')
        file_object.write(reason + '\n')
        if(reason=='not'):
            flag = False
