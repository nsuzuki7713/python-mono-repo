# https://atcoder.jp/contests/abc137/tasks/abc137_c

from collections import defaultdict

N = int(input())

# num[s]: 文字列 s が何個あるか
num = defaultdict(int)

for i in range(N):
  s = "".join(sorted(input()))

  num[s] += 1

# 集計
result = 0

for s in num:
  n = num[s]

  result += n * (n-1) // 2

print(result)