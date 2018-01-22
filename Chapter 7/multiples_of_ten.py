# Assignment 7.3
number = raw_input("Please enter a number, any number. ")
number = int(number)
if number % 10 == 0:
	print("The number you entered, " + str(number) + " is a multiple of 10 !")
else:
	print("The number you entered, " + str(number) + " is not a multiple of 10 !")
