current_users = ['rina', 'ayami', 'hanna', 'spencer', 'emily', 'aria', 'alison']
new_users = ['Alison', 'mona', 'melissa', 'AYAMI', 'haruka', 'karen']
current_users_check = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_check:
		print("Sorry, but " + new_user + " is already used. Please think of something else.")
	else:
		print(new_user + " is available !")
