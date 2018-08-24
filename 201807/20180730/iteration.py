# _*_ coding: utf-8 _*_

def diedai():
    d = {'a':1,'b':2,'c':3}
    for key in d:
        print(key, d[key])

def findMinAndMax(L):
   
    if(L==None or len(L) < 1):
        return (None,None)

    min = L[0]
    max = L[0]

    for item in L:
        if min >= item:
            min = item
        if max <= item:
            max = item
    return (min, max)

def exer():
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')

diedai()
exer()