import math

def area(r):
	"""Area of circle with radius r"""
	return math.pi*(r**2)

radii = [2,3,3.5,4]

# Method 1: Direct Method
areas = []
for r in radii:
	a = area(r)
	areas.append(a)

print(areas)

# Method 2: Use map function
a = list(map(area, radii))
print('areas =',a)
#print(list(map(area, radii)))