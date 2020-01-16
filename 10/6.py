#! /usr/bin/env python3
flag = True

while flag:
    input_1 = input('请输入一个数字')
    input_2 = input('请在输入一个数字')
    try:
        if input_1 == 'q':
            flag = False
        elif input_2 == 'q':
            flag = False
        input_1 = int(input_1)
        input_2 = int(input_2)
    except ValueError:
        print('请输入数字')
    else:
        num = input_1 + input_2
        print(str(num))
