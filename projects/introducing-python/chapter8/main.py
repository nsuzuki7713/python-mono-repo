empty_dict = {}
print(empty_dict)

bierce = {
    'day': 'A period of twenty-four hours, mostly misspent',
    'positive': 'Something that is nice',
    'negative': 'Something that is bad',
}
print(bierce)

acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)


lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

los = ['ab', 'cd', 'ef']
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

obj = {
    'a': 1,
    'b': 2,
}
obj['c'] = 3
print(obj)

some_pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
}
print(some_pythons['Chapman'])
print(some_pythons.get('Cleese'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
print(signals.values())
print(signals.items())

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'sgt. pepper'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

# 辞書内包表記
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

# 集合
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua', 'whisky'},
    'white russian': {'cream', 'kahlua', 'whisky', 'vodka'},
    'manhattan': {'whisky', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka', 'orange bitters'},
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if contents & {'vodka', 'vermouth'}:
        print(name)

# 積集合
a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))

# 和集合
print(a | b)
print(a.union(b))

# 差集合
print(a - b)
print(a.difference(b))

# 集合内包表記
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

print(frozenset([3, 2, 1]))

