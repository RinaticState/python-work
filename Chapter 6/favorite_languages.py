favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

take_poll = ['hanna', 'spencer', 'aria', 'sarah', 'jen', 'emily']

for name in take_poll:
    if name in favorite_languages:
        print("Thank you for responding, " + name.title() + "!")
    else:
        print("Hi " + name.title() + ", please take the poll.")
