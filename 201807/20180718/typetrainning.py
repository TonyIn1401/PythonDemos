print(r'''hello,\n
world''')

print('''hello,\n
world''')


print(type(1))
print(type(0.0000001))
print(type("string"))
print(type(3>2))

#一种方便的交换两个变量的值得方法，两个变量的类型都可以不一样，很棒。
a = 10
b = "a"
a,b=b,a
print("a =",a,"b =",b)

#常量，变量应该都是大写
PI = 3.14159265359

c = 10
d = 3
#常规除法得到精确的值
print("c/d=",c/d)
#地板除只取结果的整数部分
print("c//d=",c//d)
#取余数
print("c%d=",c%d)