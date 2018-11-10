"""
filter:
1) filter item out of a sequence and return filtered list.
2) syntax: filter(function, list OR tuple OR AnyIterableObject)
"""

# filter numbers which is greater than 5
def greater_than_five(lst1):
	lst2 = [x for x in lst1 if x>5]
	return lst2

print(greater_than_five([2,7,3,4,9,10,8]))

#Using filter
nums = [2,7,3,4,9,10,8]
print(list(filter(lambda x:x>5, nums)))

#Using list comprehension
print([x for x in nums if x>5])