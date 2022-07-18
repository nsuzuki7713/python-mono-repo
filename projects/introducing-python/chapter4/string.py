poem = """konnichiwa
konnichiwa
konnichiwa"""
print(poem)

# 文字列結合
print('a' + 'b')

# 文字列の繰り返し
print('a' * 3)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])

# 置き換えはすることができない
letters = 'abcdefghijklmnopqrstuvwxyz'
# エラーになる
# letters[0] = 'x'

# スライスによる文字列の取り出し
# [:] は、先頭から末尾までのシーケンス全体を抽出する。
# [start:] は、start オフセットから末尾までのシーケンスを抽出する。
# [:end] は、先頭から end -1 オフセットまでのシーケンスを抽出する。
# [start:end]は、startオフセットからend -1オフセットまでのシーケンスを抽出する。
# [start : end : step] は、step 文字ごとに start オフセットから end -1 オフセットまでのシーケンスを抽出する。
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:]) # abcdefghijklmnopqrstuvwxyz
print(letters[20:]) # uvwxyz
print(letters[2:4]) # cd
print(letters[0:3]) # abc
print(letters[::3]) # adgjmpsvy
print(letters[4:20:3]) # ehknqt

# 文字列の長さ
print(len(letters))
print(len(''))

# split()で文字列を分割する
print('a,b,c'.split(','))

# join()で文字列を結合する
print(','.join(['a', 'b', 'c']))

# replace()で文字列を置換する
print('a b c'.replace(' ', ','))

# strip()で文字列の前後の空白を削除する
print(' a b c '.strip())

# 新しいスタイル:{} と format()を使う
thing = 'woodchuck'
print('{}'.format(thing))

thing = 'woodchuck'
place = 'lake'
print('the {} is in the {}.'.format(thing, place))

thing = 'woodchuck'
place = 'lake'
print('the {1} is in the {0}.'.format(place,thing))

# f文字列を使う
think = 'wereduck'
place = 'werepond'
print(f'the {thing} is in the {place}.')

print(f'{thing =}, {place =}')