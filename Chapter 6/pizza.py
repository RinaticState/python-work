# Original sample code modified for Assignment 6.12: Extensions
# Store information about a pizza being ordered.
pizza = {
    'rina' : {
		'crust' : 'garlic',
		'toppings' : ['extra cheese'],
		'sauces' : ['marinara', 'ranch'],
		},
	'alice' : {
		'crust' : 'thick',
		'toppings' : ['bacon', 'peppers', 'onion'],
		'sauces' : [],
		},
	'blakely' : {
		'crust' : 'thin',
		'toppings' : ['pineapple', 'chicken'],
		'sauces' : ['barbucue', 'blue cheese'],
		},
    }

# Summarize the order.
for name, options in pizza.items():
	print("\n" + name.title() + " ordered the following: ")
	options_crust = options['crust']
	print("\tCrust: " + "\n\t\t" + options_crust)
	print("\tToppings: ")
	for topping in options['toppings']:
		print("\t\t" + topping)
	print("\tSauces: ")
	for sauce in options['sauces']:
		print("\t\t" + sauce)
