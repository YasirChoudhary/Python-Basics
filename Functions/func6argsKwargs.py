def student_info(*args,**kwargs):
	print(args)
	print(kwargs)

student_info('Math','Art',name="Yasi",age=22)

print("****************")
print()

course=['Math','Art']
info={
	'name':"yasir",
	'age':22
	}

student_info(course,info)

print("****************")
print()
student_info(*course,**info)