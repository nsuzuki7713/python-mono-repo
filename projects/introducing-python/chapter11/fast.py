from random import choice

places = ['home', 'school', 'work', 'restaurant', 'bar', 'cafe', 'park']

def pick():
    return choice(places)

def pick2():
    import random
    return random.choice(places)
