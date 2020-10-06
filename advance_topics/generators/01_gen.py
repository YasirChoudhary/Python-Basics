#1 Using normal method
"""
def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result

squares = square_numbers([1,2,3,4,5])

print(squares)
"""

#2 Using generator

def square_numbers(nums):
    for num in nums:
        yield (num*num)

squares = square_numbers([1,2,3,4,5])
print(squares) #Here we get generator object
#print(squares.__next__())
#print(next(squares))
#print(next(squares))
#print(next(squares))
#print(next(squares))
#print(next(squares))
#print(next(squares))
print("###############")

for sq in squares:
    print(sq)
