courses=['History', 'Maths', 'ML', 'Physics', 'CompSci']

# remove method takes one argument
courses.remove('History')
print(courses)

'''
output: ['Maths', 'ML', 'Physics', 'CompSci']
'''

'''
If we want to remove a item without passing argument we will get TypeError
courses.remove()
TypeError: remove() takes exactly one argument (0 given)

'''

courses.remove('Art')
print(courses)

'''
If we want to remove which is not in list we get ValueError

ValueError: list.remove(x): x not in list

'''
