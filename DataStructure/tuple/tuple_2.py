tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1


print(tuple_1)
print(tuple_2)

tuple_1[0]='Art'

print(tuple_1)
print(tuple_2)


'''
output:
('History', 'Math', 'Physics', 'CompSci')
('History', 'Math', 'Physics', 'CompSci')
Traceback (most recent call last):
  File "/home/yasir/Python/DataStructure/tuple/tuple_2.py", line 8, in <module>
    tuple_1[0]='Art'
TypeError: 'tuple' object does not support item assignment
'''
