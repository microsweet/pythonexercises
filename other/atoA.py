def normalize(name):
    flag = True
    b = ''
    for word in name:
        a = ''
        if flag:
            a = word.upper()
            flag = False
        else:
            a = word.lower()
        b = b + a
    return b


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
