disaster = True

if disaster:
    print("The world is in danger!")
else:
    print("The world is safe!")

color = 'mauve'

if color == 'blue':
    print('The color is red')
elif color == 'green':
    print('The color is green')
elif color == 'blue':
    print('The color is blue')
else:
    print('The color is not red, green or blue')

x = 7
if (5 < x and x < 10):
    print('x is between 5 and 10')
else:
    print('x is not between 5 and 10')

if (5 < x < 10):
    print('x is between 5 and 10')
else:
    print('x is not between 5 and 10')

# inによる多重比較
vowels = 'aeiou'
letter = 'o'
if letter in vowels:
    print('The letter is a vowel')

# セイウチ演算子
tweet_limit = 280
tweet_string = "Blah" * 50
if (diff := tweet_limit - len(tweet_string)) >= 0:
    print("A fitting tweet")
else:
    print("went over by", abs(diff))
