num = int(input())

def func(num)
	if num  % 10 == 1 and num  % 100 != 11: #+условие на 11,111...
		print(num ,'программист')
	elif num  % 10 >= 2 and num  % 10 <=4 and (num  %100 < 10 or num  %100 >= 20): #условие на 12,13, 112
		print(num ,'программиста')
	else:
		print(num ,'программистов')
	
print(func(num))
