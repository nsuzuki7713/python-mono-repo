# https://atcoder.jp/contests/abc088/tasks/abc088_b

N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

alice_card_point = 0
bob_card_point = 0

for i in range(N):
  if i % 2 == 0:
    alice_card_point += a[i]
  else:
    bob_card_point += a[i]

print(alice_card_point - bob_card_point)