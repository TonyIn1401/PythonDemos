# _*_ coding: utf-8 _*_
from functools import reduce

def add(x,y, f):
    return f(x) + f(y)

def f(x):
    return x*4

def fn(x, y):
    return str(x) + str(y)

def pra():
    L = range(10)
    print(reduce(fn,L))
    print(list(map(f,L)))
    print(add(-1,-2,abs))

def firtoup(words):
    if(not isinstance(words, str)):
        words = str(words)
    if(len(words)<1):
        return words
    return words[0].upper()+ words[1:].lower()

def prod(L):
    return reduce(lambda x,y: x*y, L)

def str2float(s):
    if('.' in s):
        L = s.split('.',1)
        sz = reduce(lambda x,y: int(x)*10+int(y), L[0])
        sx = int(L[1])* pow(10,-len(L[1]))
        return float(sz)+float(sx)

def strtofloat(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(x):
        return DIGITS[x]
    _index=s.find('.')
    s1=s[0:_index]
    s2=s[-1:_index:-1] + '0'
    a1=reduce(lambda x, y: x * 10 + y, map(char2num, s1))
    a2=reduce(lambda x, y: x * 0.1 + y, map(char2num, s2))
    return a1 + a2

def exer():
    L = ['adam', 'LISA', 'barT']    
    print(list(map(firtoup,L)))

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    print('str2float(\'123.456\') =', strtofloat('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

    print("Test")

exer()
pra()