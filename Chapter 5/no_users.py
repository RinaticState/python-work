# Detects to see if there are any users.
usernames = []
if usernames:
	for username in usernames:
		if username == 'admin':
			print("Greetings, admin. Would you like to see an activity log ?")
		else:
			print("Hello " + username.title() + ", thanks for logging in again.")
else:
	print("We need to find some users !")
