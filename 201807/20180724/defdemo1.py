#_*_ coding: utf-8 _*_

def demo1():
	print(abs(-100))
	n1 = 100
	n2 = 255
	print(hex(n1))
	print(bin(n2))
	
def return_onevalue(x):
	if x >= 0:
		return x
	else:
		return -x

def return_twovalue(x):
	if x >= 0:
		return x, True
	else:
		return -x, False
		
def product(x, *numbers):
	sum = x
	if len(numbers) > 0:
		for num in numbers:
			sum = sum * num
	return sum
	
def validate():
	print('product(5) =', product(5))
	print('product(5, 6) =', product(5, 6))
	print('product(5, 6, 7) =', product(5, 6, 7))
	print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
	if product(5) != 5:
		print('测试失败!')
	elif product(5, 6) != 30:
		print('测试失败!')
	elif product(5, 6, 7) != 210:
		print('测试失败!')
	elif product(5, 6, 7, 9) != 1890:
		print('测试失败!')
	else:
		try:
			product()
			print('测试失败!')
		except TypeError:
			print('测试成功!')
validate()
print(return_onevalue(-100))
print(return_twovalue(-100))
demo1()