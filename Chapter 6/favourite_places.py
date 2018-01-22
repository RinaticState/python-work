# Assignment 6.9

favourite_places = {
	'aria' : ['ohio', 'wisconsin', 'new york', 'massachusetts'],
	'haruka' : ['new mexico', 'pennsylvania', 'california'],
	'rina' : ['tokyo', 'london', 'saigon'],
	}
	
for person, places in favourite_places.items():
	print("\n" + person.title() + "'s favourite places are: ")
	for place in places:
		print("\t" + place.title())
