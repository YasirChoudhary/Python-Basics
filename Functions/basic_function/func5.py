def hello_func(greeting, name="you"):
	return "{}, {}".format(greeting,name)

print(hello_func("Hi","Yasir"))

print(hello_func("hello",name="Reza"))