# _*_ coding: utf-8 _*_

def dic_exer1():
	d = { 'michael': 12, 'tony': 13, 'bonnie':14}
	print(d['tony'])
	d["jesscia"] = 15
	print(d)	
	d.pop('tony')
	print(d)
	
	print("mi" in d)
	print(d.get("mi",-1))
	
def set_exer1():
	s1 = set([1,2,3])
	s2 = set([2,3,'4'])
	#set添加元素
	s1.add('4')
	#set删除元素
	s2.remove(3)
	print(s1 & s2)

dic_exer1()
set_exer1()