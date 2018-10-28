# Compare two numbers and return the greater number.
def mx(x,y):
	if x>y:
		return x
	else:
		return y

greter_num = mx(4,5)
print(greter_num)


# lambda expression of above function
mx = lambda x,y: x if x>y else y
greater_number = mx(8,10)
print(greater_number)