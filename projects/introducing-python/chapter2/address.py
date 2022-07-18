# https://wayama.io/article/library/python/003/
a = 5
b = a
print('同じアドレスを指す')
print(id(a))
print(id(b))

b = 2
print('別の値を入れると別のアドレスを指す')
print(id(a))
print(id(b))

