# https://atcoder.jp/contests/abc085/tasks/abc085_b

# バケットサイズ
M = 101

N = int(input())

# バケット(全体を0で初期化)
exist = [0] * M

for i in range(N):
  d = int(input())

  exist[d] = 1

print(sum(exist))