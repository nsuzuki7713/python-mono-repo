# https://atcoder.jp/contests/abc165/tasks/abc165_a

k = int(input())
a, b = map(int,input().split())
exist = False

for i in range(a, b + 1):
  if i % k == 0:
    exist = True

print("OK" if exist else "NG")