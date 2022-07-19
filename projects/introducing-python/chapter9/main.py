def do_nothing():
    # このページを意図的に空白にするのと同じことになる(pass文)
    pass

do_nothing()

def make_a_sound():
    print("Quack!")

make_a_sound()

def agree():
    return True

if agree():
    print("You agreed!")
else:
    print("You disagreed!")

def echo(anything):
    return anything + ' ' + anything

print(echo('hello'))

def commentary(color):
    if color == 'red':
        return 'It\'s a tomato'
    elif color == 'green':
        return 'It\'s a green pepper'
    elif color == 'bee purple':
        return 'I don\'t know what it is, but only bees can see it'
    else:
        return 'I have no idea'

comment = commentary('red')
print(comment)

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

def menu2(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

def buggy(arg, result = []):
    result.append(arg)
    return result

# デフォルト引数の値が計算されるのは、関数が実行されたときではなく、 定義されたとき
print(buggy('a')) # ['a']
print(buggy('b')) # ['a', 'b']

# 関数定義の中で仮引数の一部として * を使うと、可変個の位置引数がタプルにまとめられてその仮引数にセットされるようになる。
def print_args(*args):
  print('Positional tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

# 2 つのアスタリスク(**)を使えば、キーワード引数を 1 個の辞書にまとめることができる
def print_kwargs(**kwargs):
  print('Keyword arguments:', kwargs)

print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# キーワード引数がない場合はエラーになる
# print_kwargs('merlot')

# Python 3では、キーワード専用引数を指定できるようになった。名 前からもわかるように、この種の引数は、位置引数として value という形では渡せず、 name=value というキーワード引数の形で渡さなければならない。
def print_data(data, *, start=0, end=100):
  for value in (data[start:end]):
    print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print_data(data, start=4)
print_data(data, end=2)

def answer():
    return 42

def run_something(func):
    print(func())

run_something(answer)

# 関数内関数
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

# クロージャー
def knights2(saying):
    def inner2():
        return f"We are the knights who say: '{saying}'"
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a())
print(b())

# 無名関数（ラムダ関数）
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')

# ジェネレータ
# ジェネレータは、Python のシーケンスを作成するオブジェクトである。ジェネレー タを使えば、シーケンス全体を一度に作ってメモリに格納しなくても、(巨大になるこ とがある)シーケンスを反復処理できる。
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)
for x in ranger:
    print(x)

# デコレータ
# デコレータは、入力として関数を 1 つ取り、別の関数を返す関数である。
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

# 手作業でデコレータを作る
cooler_add_items = document_it(add_ints)
cooler_add_items(3, 5)

# デコレートしたい関数の 直前に @decorator_name をつけることもできる。
@document_it
def add_ints2(a, b):
    return a + b

add_ints2(3, 5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints3(a, b):
    return a + b

add_ints3(4, 5)

short_list = [1, 2, 3]
position = 5

try:
    short_list[position]
except IndexError as e:
    print(e)
except Exception as e:
    print(e)