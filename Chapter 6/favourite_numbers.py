# Assignment 6.2, remodified for assignment 6.10

favourite_numbers = {
	'spencer' : [100, 200, 300],
	'emily' : [0, 1, 2, 3],
	'hanna' : [4050, 9999, 1234],
	'aria' : [26, 52, 78],
	'alison' : [16, 17, 18],
	}

for name, numbers in favourite_numbers.items():
	print("\n" + name.title() + "'s favourite numbers are: ")
	for number in numbers:
		print("\t" + str(number))
