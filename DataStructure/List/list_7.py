courses=['History', 'Maths', 'ML', 'Physics', 'CompSci']

courses_2 = ["Datawarehouse","ComputerGraphics"]

courses.insert(0,courses_2) # in this method the whole list is inserted at index 0
#This is not a good way to insert a list

print(courses)
'''
output: [['Datawarehouse', 'ComputerGraphics'], 'History', 'Maths', 'ML', 'Physics', 'CompSci']

'''

print(courses[0])
'''
output: ['Datawarehouse', 'ComputerGraphics']
'''
