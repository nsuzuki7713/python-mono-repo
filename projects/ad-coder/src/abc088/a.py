# https://atcoder.jp/contests/abc088/tasks/abc088_a

n = int(input())
a = int(input())

hasu = n % 500
if hasu == 0:
  print("Yes")
elif hasu <= a:
  print("Yes")
else:
  print('No')