"""
map function:
1) Apply same function to each element of a sequence and it return modified list.
2) map function takes two argument first one is function and second argument is
   list, tuple or other iterable object.
"""
# calculate square of each element in a list
def square(lst1):
	lst2 = []
	for num in lst1:
		lst2.append(num**2)
	return lst2

print(square([2,3,4,5]))

# Using map and lambda function
n = [2,3,4,5]
print(list(map(lambda num: num**2, n)))

# List comprehension solution
print([num**2 for num in n])

