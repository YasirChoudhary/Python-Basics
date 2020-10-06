"""
We use decorator to modify existing functions behaviour and to add extra 
features in it
"""
def check_div(func):
    def inside_func(a,b):
        if b==0:
            print("Can't divide by zero")
            return 
        func(a,b)
    return inside_func

def div(a,b):
    return a/b

div = check_div(div)
print(div(4,0))
