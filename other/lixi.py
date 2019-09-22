a = 410000
def bb(bj, i):
    
    if i < 3:
        i += 1
        return bb(bj*1.03575, i)
    else:
        return bj*1.03575

d = bb(a, 1)
print(d)
