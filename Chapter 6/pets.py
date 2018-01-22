# Assignment 6.8

aria = {
	'name' : 'aria',
	'kind' : 'dog',
	'owner' : 'aria jordan',
	}
	
alice = {
	'name' : 'alice',
	'kind' : 'mallard duck',
	'owner' : 'nghi nguyen',
	}
	
everett = {
	'name' : 'everett',
	'kind' : 'fish',
	'owner' : 'brenda chen',
	}
	
rachel = {
	'name' : 'rachel',
	'kind' : 'goose',
	'owner' : 'rachel chong',
	}
	
pets = [aria, alice, everett, rachel]

for pet in pets:
	print(pet['name'].title() + " is a " + pet['kind'] + " and owned by " + pet['owner'].title() + ".")
