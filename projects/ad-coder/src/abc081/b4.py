# https://atcoder.jp/contests/abc081/tasks/abc081_b

# 整数 num が 2で何回割れるか
def how_many_times(num):
  counter = 0

  while num % 2 == 0:
    num //= 2

    counter += 1
  
  return counter

# 十分大きな値を初期化
INF = 2 ** 30

N = int(input())
A = list(map(int, input().split()))

result = min(map(how_many_times, A))

print(result)