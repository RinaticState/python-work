# A list of 3D Grand Theft Auto Games
games = ['iii', 'vice city', 'san andreas', 'vice city stories', 'liberty city stories']

# Ewmocing Vice City Stories from the list
popped_vcs = games.pop(-2)
print("\nI have played all the games in the 3D Grand Theft Auto Universe except for " + popped_vcs.title())
# The list should look like III, Vice City, San Andreas, Liberty City Stories

# Adding GTA IV and GTA V
games.insert(4, 'iv')
games.append('v')

# Using the sorted() method to alphabetise the list
print("\nI've completed some more games, here they are alphabetised.")
print(sorted(games))

# Using .remove() to get rid of GTA V
terrible_game = 'v'
games.remove(terrible_game)
print("\nContrary to popular opinion, I didn't enjoy " + terrible_game.title()) + "."

print("\nHere is what the list looks like now:")
print(games)

# Reversing the list
print("\nHere is the list in reverse order")
games.reverse()
print(games)

# Reverse alphabetical order of the list
print("\nHere's that list in reverse alphabetical order:")
print(sorted(games, reverse=True))

favourite_game = "\nI enjoyed " + (games[2]).title() + " the most."
print(favourite_game)
