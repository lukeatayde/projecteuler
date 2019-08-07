import math
from collections import defaultdict

def proper_divisors(val):
	"""
	INPUT: val, an integer for the upper bound of the dictionary to generate
	OUTPUT: a list of all the proper divisors of a number
	"""
	divisors = []
	for i in range(1, 1+int(math.sqrt(val))):
		if val % i == 0:
			divisors.append(val / i)
			divisors.append(val / divisors[-1])
	divisors = list(set(divisors))
	divisors.sort()
	if divisors:
		divisors.pop(-1)
	return [int(x) for x in divisors]

def pds(val):
	"""
	INPUT: An integer
	OUTPUT: The sum of its proper divisors less than that number
	"""
	return sum(proper_divisors(val))

def is_amicable(lookup, val):
	"""
	INPUT:
		lookup - a default dict to be used as a lookup table for the sum of proper divisors
		val - an integer to test if there exists an amicable number
	OUTPUT: the amicable number of val if one exists. Otherwise, 0
	"""
	if val not in lookup:
		lookup[val] = pds(val)
	if lookup[val] not in lookup:
		lookup[lookup[val]] = pds(lookup[val])
	if val == lookup[lookup[val]] and val != lookup[val]:
		print(f"VAL: { val }, lookup[val]: { lookup[val] }, lookup[lookup[val]]:{ lookup[lookup[val]]}")
		return lookup[lookup[val]]
	return 0

def sum_amicable(index):
	"""
	INPUT: index - integer upper bound to calculate the sum off all amicable nums of
	OUTPUT:	sum - the summation of all the amicable numbers under the bound index
	"""
	lookup_table = {}
	sum = 0
	for i in range(index):
		if is_amicable(lookup_table, i):
			sum += i
	return sum

# print(proper_divisors(25))
# print(proper_divisors(220))
# print(sum_amicable(10))

print(sum_amicable(10000))




