filename = 'guest_book.txt'
flag = True
with open(filename, 'a') as file_object:
    while flag:
        name = input('请输入用户名：')
        print(name + '，你好')
        file_object.write(name + '\n')
        if name == 'stark':
            flag = False
