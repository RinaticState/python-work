programming_words = {
    'tuples' : 'immutable sequences',
    'slice' : 'specific group of items in a list',
    'float' : 'any number with decimal point',
    'list' : 'collection of items in a particular order',
    'type error' : 'an exception thrown due to data type',
    'dictionary' : 'a collection of key-value pairs',
    'key-value pair' : 'set of values associated with each other',
    'logical error' : 'syntax is valid, but result is not expected',
    'append' : 'adding an item to the end of a list',
    'method' : 'action Python performs on a piece of data',
    }

for word, definition in sorted(programming_words.items()):
    print("\n" + word)
    print("\t" + definition)
