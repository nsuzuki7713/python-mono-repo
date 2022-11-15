a, b = map(int, input().split())
c = a * b

# if c % 2 == 0:
#   print('Even')
# else:
#   print('Odd')

# 3項演算子で書くとこうなる
print("Even" if c % 2 == 0 else "Odd")