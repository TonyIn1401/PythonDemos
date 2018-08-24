#_*_ coding: utf-8 _*_
def fact(n):
	if n == 1:
		return 1
	return n + fact(n-1)
	
def fact_iter(n, sum = 1):
	if n == 1:
		return sum
	return fact_iter(n-1, sum + n)

#sum1 = fact(1000)
sum2 = fact_iter(1000)

print(sum2)