"""
lmbda expression:
- A simple 1-line function.
- Do not use def or return keywords. These are implicit. 
- lambda expression is also known as 'Anonymous Function'
- lambda expression is expressed as:

	lambda argument: return_expression

"""
def double(x):
	return 2*x

print(double(4))

"""
lambda x: 2*x
- There is a problem about lambda function, We cannot use lambda because it doesn't have a name.
- lambda is not a name of a function.
- lambda is a keyword in python that follows a anonymous function in python.
- one way to give a name of lambda function:
	f = lambda x: 2*x
"""

# lambda expression of above function.
f = lambda x: 2*x
print(f(4))