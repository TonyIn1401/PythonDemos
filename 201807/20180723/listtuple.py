def For_Print(listObj):
    index = 1
    for item in listObj:
        print('the {} item in listObj is {}'.format(index, item))
        index += 1
		
def classMatesShow():
    classMates = ['Michael', 'Bob', 'Tony']    
    print(classMates)
	
    classMates.append('Bonnie')    
    print(classMates)
    
    classMates.insert(1, 'Jessica')    
    print(classMates)
    
    classMates.pop()    
    print(classMates)
    
    classMates.pop(1)    
    print('classMates\'s lenth is {}'.format(len(classMates)))   
    
    For_Print(classMates)
	
def LShow():
    L = ['Apple', 123, True, 1.23]
    P = ['python', 'java', L, 'php']
    print(P)

def PracticeDemo():
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
	]
	
	# 打印Apple:
    print(L[0][0])
    # 打印Python:
    print(L[1][1])
    # 打印Lisa:
    print(L[2][2])
	
	
LShow()
classMatesShow()
PracticeDemo()