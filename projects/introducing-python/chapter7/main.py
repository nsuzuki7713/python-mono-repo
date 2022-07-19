empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

one_marx = ('Groucho',)
print(one_marx)

# カンマがないとタプルにならない
one_marx = ('Groucho')
print(one_marx)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

a, b, c = marx_tuple
print(a)
print(b)
print(c)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

words = ('fresh', 'fresh', 'and', 'jelly')
for word in words:
    print(word)

# リストは、要素を順番に管理したいとき、特に順序と内容が変わる場合があるときに 向いている。文字列やタプルとは異なり、リストはミュータブルだ。リストの内容は直 接変更できる。新しい要素を追加したり、既存の要素を削除、置換したりできる。
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)

# リストのコピー
# b、c、d は、a のコピーである
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'lundi', 'mardi', 'mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))

# リスト内包表記
number_list = [number for number in range(1, 6)]
print(number_list)

number_list = [number - 1 for number in range(1, 6)]
print(number_list)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)