# https://atcoder.jp/contests/abc153/tasks/abc153_a

h, a = map(int, input().split())

if h % a == 0:
  print(h // a)
else:
  print(h // a + 1)