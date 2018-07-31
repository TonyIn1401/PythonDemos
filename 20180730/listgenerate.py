# _*_ coding: utf-8  _*_
import os

def generateList():
    L1 = [x*x for x in range(1,11)]
    print(L1)
    L2 = [x*x for x in range(1,11) if x%2 == 0]
    print(L2)
    L3 = [m+n for m in 'xyz' for n in 'abc']
    print(L3)
    L4 = [d for d in os.listdir('.')]
    print(L4)
    L5 = [i.upper() for i in L4]
    print(L5)

def exer():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [x.lower() for x in L1 if isinstance(x, str)]
    # 测试:
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')

exer()
generateList()