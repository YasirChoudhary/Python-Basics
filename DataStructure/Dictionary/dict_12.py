student = {'name': 'Yasir', 'id': 22, 'courses': ['Math', 'CompSci']}

age = student.pop('id')
print(student)
print('popped element : ',age)

'''
Output:
{'name': 'Yasir', 'courses': ['Math', 'CompSci']}
popped element :  22
'''
