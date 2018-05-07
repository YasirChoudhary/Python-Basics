courses=['History', 'Maths', 'ML', 'Physics', 'CompSci']

# remove method takes one argument
courses.remove('Art')
print(courses)

'''
output: ValueError: list.remove(x): x not in list
'''

'''
suppose if we have a large list of items and we want to remove a item
which is not present in the list we will get ValueError.
If the item is present remove method will remove the element.

ValueError: list.remove(x): x not in list

'''
