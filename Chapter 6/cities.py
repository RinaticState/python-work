# Assignment 6-11

cities = {
	'ho chi minh' : {
		'country' : 'vietnam',
		'population' : 8426000,
		'fact' : 'Renamed from Saigon post the Vietnam war',
		},
	'nagoya' : {
		'country' : 'japan',
		'population' : 2296000,
		'fact' : 'Capital of Aichi Prefecture',
		},
	'moscow' : {
		'country' : 'russia',
		'population' : 112900000,
		'fact' : 'Thought to be built upon swamp',
		},
	}
	
for city, city_info in cities.items():
	print("\nCity: " + city.title())
	city_country = city_info['country']
	city_population = city_info['population']
	city_fact = city_info['fact']
	print("\tCountry: " + city_country.title())
	print("\tPopulation: " + str(city_population))
	print("\tFact: " + city_fact + ".")
