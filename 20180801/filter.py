# _*_ coding: utf-8 _*_

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def sushu(n):
    return lambda x: x % n > 0

def promis():
    yield 1
    yield 2
    L = _odd_iter()
    while True:
        n = next(L)
        yield n
        L = filter(sushu(n), L)

def show():
    n = promis()
    L = []
    for i in n:
        if(i <1000):
            L.append(i)
        else:
            break
    print (L)

def is_palindrome(n): 
    if(not isinstance(n,int)):
        return False
    s = str(n)
    return s == s[::-1]

def exer():
    # 测试回数:
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')

exer()
#show()
