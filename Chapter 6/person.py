person = {
	'first_name' : 'ayami',
	'last_name' : 'nakajo',
	'age' : 20,
	'city' : 'tokyo',
	}
	
print(person['first_name'].title() + " " + person['last_name'].title() + " is " + str(person['age']) + " and lives in " + person['city'].title() + ".")

person_1 = {
	'first_name' : 'ginta',
	'last_name' : 'lapina',
	'age' : 27,
	'city' : 'new york',
	}
	
person_2 = {
	'first_name' : 'nastya',
	'last_name' : 'kusakina',
	'age' : 22,
	'city' : 'moscow',
	}

people = [person, person_1, person_2]

for someone in people:
	print(someone['first_name'].title() + " " + someone['last_name'].title() + " is " + str(someone['age']) + " and lives in " + someone['city'].title() + ".")
