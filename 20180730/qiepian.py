# _*_ coding: utf-8 _*_
def sep(words):
    print()
    print("---------------{}----------------".format(words))

def qiepian():
    L = list(range(10))
    print(L)

    sep("整数切片")
    print("L[0:9]:",L[0:9])
    print("L[:5]:",L[:5])
    print("L[8:]:",L[8:])

    sep("负数切片")
    print("L[-2:]:",L[-2:])
    print("L[-6:-1]:",L[-6:-1])
    print("L[:-6]:",L[:-6])
    print(L[1:-1])
    
    sep('每隔2个取一个')
    N =list(range(100))
    print(N[:10:2])

    sep('切片复制list')
    B = L   
    M =L[:]
    L[0] = 1
    print(B)
    print(L)
    print(M)

    sep("tuple切片")
    Q = (1,2,3,4,5)
    print(Q[:4])

    sep("string切片")
    S = "Hello World!"
    print(S[6:])

def trim(stringParams):
    if stringParams == '':
        return stringParams
    elif stringParams[0] == ' ':
        return trim(stringParams[1:])
    elif stringParams[-1] == ' ':
        return trim(stringParams[:-2])
    else:
        return stringParams

def exer():
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')

exer()
qiepian()
