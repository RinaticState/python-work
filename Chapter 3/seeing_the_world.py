# A list of places I'd like to visit
print("Here is a list of 5 places I'd like to visit")
places = ['paris', 'provincetown', 'london', 'nagoya', 'hanoi']
print(places)

# Using the sorted() to alphabetise the list
print("\nHere is the list in alphabetical order;")
print(sorted(places))
print("\nThe list is still the same.")
print(places)

# Reverse alphabetise the list
print("\nHere is the list in reverse alphabetical order:")
print(sorted(places, reverse=True))
print("\nThe list is still the same.")
print(places)

# Using reverse() to modify the order of the list
print("\nHere is a reverse order of the list.")
places.reverse()
print(places)

# Undoing the reverse()
print("\nThe list is back in its original order.")
places.reverse()
print(places)

# Permantely alphabetising the list using sort()
print("\nHere is the list in alphabetised order.")
places.sort()
print(places)

# Reverse alphabetising the list still using sort()
print("\nHere is the list in reverse alphabetical order.")
places.sort(reverse=True)
print(places)
