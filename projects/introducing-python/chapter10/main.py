class Cat:
    pass

a_cat = Cat()
another_cat = Cat()

a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat
a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.name)
print(a_cat.nemesis.name)

class Cat:
    # コンストラクタ
    # 第一引数でselfを受け取る
    # Pythonは __init__() を呼び出す前にすでにオブジェクトを構築している。__init__() はイニシャライザ(初期化子)と考えるべきだ。
    def __init__(self, name):
        self.name = name

furball = Cat("Grumpy")
print(furball.name)

class Car:
    pass

class Yugo(Car):
    pass

# 継承したものかどうか
print(issubclass(Yugo, Car))

class Car:
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# オーバライド
class Car:
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Person:
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
      
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

# 多重継承
class Animal:
    def says(self):
      return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())

# ゲッターとセッター
# Python は非公開属性を持っていないが、属性名を少し非公開っぽくわかりにくくし た上でゲッター、セッターを書くことはできる(ただし、最良の方法は、次節で説明す るプロパティである)。
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

dom = Duck('Donald')
print(dom.get_name())
dom.set_name('Daffy')
print(dom.get_name())

# プロパティ
# 属性の非公開化のためのパイソニックな方法は、プロパティである
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

dom = Duck('Donald')
print(dom.name)
dom.name = 'Daffy'
print(dom.name)

# @property:ゲッターメソッドの前に付けるデコレータ
# @name.setter:セッターメソッドの前に付けるデコレータ。
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

dom = Duck('Donald')
print(dom.name)
dom.name = 'Daffy'
print(dom.name)

# 計算された値のためのプロパティ
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.radius)
print(c.diameter)

# 属性を隠すための名前のマングリング
# Python は、クラス定義の外からは見えないようにすべき属性の命名方法を持つ。先頭に2つのアンダースコア(__)を付けるのである。
class Duck:
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
# エラーになる
# print(fowl.__name)

# このようにしてアクセスすることはできる
print(fowl._Duck__name)

# クラス属性
class Fruit:
    color = 'red'

print(Fruit.color)

# インスタンスメソッド
# クラス定義の中でメソッドの第 1 引数が self になっていたら、それはインスタンスメソッドであり、独自クラスを作るときに普通書くタイプのメソッドである。

# クラスメソッド
# クラス定義の中で、デコレータ @classmethodを入れると、その次のメソッドはクラスメソッドになり、メソッドの第 1 引数は、クラ ス自体になる。
class A:
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print('A has', cls.count, 'little objects.')

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

# 静的メソッド
# 独立した存在としてふらふらしているよりも都合がよいのでクラス 定義の中にいるだけだ。それは、@staticmethodデコレータを付けた静的メソッド である。
class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('It\'s a weapon for commercial use.')
    # staticとの違いは、クラスを引数に取るかの違いかな。
    @classmethod
    def commercial2(cls):
        print('It\'s a weapon for commercial use2.')

CoyoteWeapon.commercial()
CoyoteWeapon().commercial2()

# ダックタイピング
# Python は、ポリモーフィズムの緩やかな実装を持つ。クラスの種類にかかわらず、 メソッドの名前と引数に基づき、異なるオブジェクトに対して同じ操作を適用するのである。
class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class BabblingBrook:
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

def who_says(obj):
    print(obj.who(), 'says:', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(BabblingBrook())

# 特殊メソッド
class Word:
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)

class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill, and a', self.tail.length, 'tail.')

a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

# データクラス
class TeenyClass:
    def __init__(self, name):
        self.name = name

tenny = TeenyClass('itsy')
print(tenny.name)

from dataclasses import dataclass
@dataclass
class TeenyClass:
    name: str

tenny = TeenyClass('bitsy')
print(tenny.name)