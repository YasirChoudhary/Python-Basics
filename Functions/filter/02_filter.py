#find all data above the avg and belo avg

import statistics
data = [2,2.3,7,1,5.5,9,13,15]

avg = statistics.mean(data)
print('mean = ',avg)

#
def above_avg(lst):
	lst2 = [x for x in lst if x>avg]
	return lst2

print(above_avg(data))


def below_avg(lst):
	lst2 = [x for x in lst if x<avg]
	return lst2

print(below_avg(data))

#Using filter: data above avg
print(list(filter(lambda x: x>avg, data)))

#Using filter: data below avg
print(list(filter(lambda x: x<avg, data)))