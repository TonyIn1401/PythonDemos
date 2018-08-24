# _*_ coding: utf-8 _*_

def sortdemo():
    L = [5, 9, -12, -21, 36]
    L = sorted(L, key = abs)
    print(L)
    L = sorted(L, reverse = True)
    print(L)

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

def exer():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)
    L3 = sorted(L, key=by_score)
    print(L2)
    print(L3)

sortdemo()
exer()