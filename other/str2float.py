from functools import reduce

def str2float(s):
    index = s.index('.')
    upNum = s[:index]
    downNum = s[index+1:][::-1]
    return reduce(upDot, map(getNum, upNum))+reduce(downDot, map(getNum, downNum))/10
    
def getNum(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]
def upDot(x, y):
    return x*10+y
def downDot(x, y):
    return x/10+y

print('str2float(\'123.456\') = ', str2float('123.456'))

if abs(str2float('123.456') - 123.456) <0.00001:
    print('success')
else:
    print('error')
