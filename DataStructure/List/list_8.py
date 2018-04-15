courses=['History', 'Maths', 'ML', 'Physics', 'CompSci']
courses_2 = ["Datawarehouse","ComputerGraphics"]

# extend method is a good way to extend a list in another list

courses.extend(courses_2)
print(courses)
'''
output:
['History', 'Maths', 'ML', 'Physics', 'CompSci', 'Datawarehouse', 'ComputerGraphics']
'''

