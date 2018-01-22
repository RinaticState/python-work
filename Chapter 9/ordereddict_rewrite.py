from collections import OrderedDict

programming_words = OrderedDict()

programming_words['tuples'] = 'immutable sequences'
programming_words['slice'] = 'specific group of items in a list'
programming_words['float'] = 'any number with a decimal point'
programming_words['list'] = 'collection of items in a particular order'
programming_words['type error'] = 'an exception thrown due to data type'
programming_words['dictionary'] = 'a collection of key value pairs'
programming_words['key-value pair'] = 'set of values associated with each other'
programming_words['logical error'] = 'syntax is value, but result is not expected'
programming_words['append'] = 'adding an item to the end of a list'
programming_words['method'] = 'action Python performs on a piece of data'

"""
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
"""

for word, definition in programming_words.items():
    print("\n" + word)
    print("\t" + definition)
