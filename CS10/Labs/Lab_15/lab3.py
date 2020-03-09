def split_into_digits(num):
	"""
	Returns a list of the individual digits of a number

	>>>split_into_digits(145)
	[1, 4, 5]
	"""
	return [int(i) for i in str(num)]

# Warm-up

# Exercise 1.1
def is_factorion(num):
	tracker = 1
	for i in split_into_digits(num):
		for i2 in range(1, i+1):
			tracker *= i2
		num -= tracker
		tracker = 1
	return num == 0

# Exercise 1.2
def list_all_factorions_between(start, end):
	return [i for i in range(start, end+1) if is_factorion(i)]


# Exercise 2.1
def is_pandigital(num):
	return not False in [str(i) in str(num) for i in range(1, len(str(num)) + 1)]

# Exercise 2.2
def list_all_pandigital_between(start, end):
	return [i for i in range(start, end+1) if is_pandigital(i)]

# Exercise 3
def list_satisfying_numbers_between(predicate, start, end):
	return [i for i in range(start, end + 1) if predicate(i)]
