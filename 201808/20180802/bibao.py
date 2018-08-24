# _*_ coding: utf-8 _*_

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n+=1
        return n   
    return counter

def exfunc(n):
    sum = n
    def insfunc():
        return sum +1
    return insfunc


def exer():
    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

initLoc = [0,0]
def createPos(pos = initLoc):
    def mov(direc,step):
        pos[0] = pos[0] + direc[0]*step
        pos[1] = pos[1] + direc[1]*step
        return pos
    return mov


def practice():
    myfunc = exfunc(10)
    print(myfunc())

    player1 = createPos()
    print(player1([0,1],3))
    print(player1([1,0],3))

    L = list(filter(lambda x: x% 2 == 1, range(1, 20)))
    print(L)

practice()