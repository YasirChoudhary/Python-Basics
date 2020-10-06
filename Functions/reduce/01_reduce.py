"""
reduce function: It is used to reduce a sequence of elements to a single value by processing the elements according to a function supplied it returns a single value.

It is a part of functools module so you have to import it

Syntax:
reduce(function, sequence)
"""
from functools import reduce
n = [1,2,3,4,5,6,7,8,9]

result = reduce(lambda x,y:x+y, n)
print(result)

#Alternate method
sum=0
for num in n:
    sum +=num
print(sum)
