# https://atcoder.jp/contests/abc083/tasks/abc083_b

n, a, b = map(int, input().split())

sum = 0

for i in range(1, n + 1):
  t = 0
  for j in list(str(i)):
    t += int(j)
  
  if a <= t and t <= b:
    sum += i

print(sum)
