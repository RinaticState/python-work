# Creates a personalised message for the admin while giving generic
# greetings to normal users.
usernames = ['admin', 'rina', 'rena', 'rila', 'reina', 'roko']
for username in usernames:
	if username == 'admin':
		print("Greetings, admin. Would you like to see an activity log ?")
	else:
		print("Hello " + username.title() + ", thanks for logging in again.")
