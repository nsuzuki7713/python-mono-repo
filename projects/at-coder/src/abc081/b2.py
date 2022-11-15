N = int(input())
A = list(map(int, input().split()))

counter = 0

while all(a % 2 == 0 for a in A):
  A = [a // 2 for a in A]

  counter += 1

print(counter)