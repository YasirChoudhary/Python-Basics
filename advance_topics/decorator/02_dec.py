def check_div(func):
    def inside_func(a,b):
        if b==0:
            print("Can't divide by zero")
            return  
        else:
            return func(a,b)
    return inside_func

@check_div
def div(a,b):
    return a/b

print(div(4,2))

