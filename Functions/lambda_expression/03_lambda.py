# Combine first_name and last_name into a single full_name

def full_name(fn,ln):
	return fn.strip().title()+ " " +ln.strip().title()

print(full_name(" yasir", " cHOUdhary"))


# lambda expression of above function
name = lambda fn,ln: fn.strip().title()+ " " +ln.strip().title()
print(name(" cHoudHary", "yasir"))