def factorial(val):
	"""
	INPUT: An integer
	OUTPUT: val!
	"""
	if val == 1 or val == 1:
		return 1
	return val * factorial(val-1)


print(factorial(100))
print(sum([int(digit) for digit in str(factorial(100))]))
