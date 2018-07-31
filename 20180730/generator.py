# _*_ coding: utf-8 _*_

def generat1():
    g = (x*x for x in range(10))
    for item in g:
        print(item)

def flb(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n+=1

def generat2():
    g1 = flb(10)
    for item in g1:
        print(item)    


generat1()
generat2()