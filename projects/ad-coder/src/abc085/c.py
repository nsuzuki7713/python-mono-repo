# https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int, input().split())

# 答えを格納するための変数
ares, bres, cres = -1, -1, -1

# 全探索
# for a in range(N+1):
#   for b in range(N+1):
#     for c in range(N+1):
#       if a + b + c == N and 10000 * a + 5000 * b + 1000 * c == Y:
#         ares, bres, cres = a, b, c

# 全探索の改良版
for a in range(N+1):
  for b in range(N+1):
    c = N - a - b

    if c < 0 or c > N:
      continue
    
    if 10000 * a + 5000 * b + 1000 * c == Y:
        ares, bres, cres = a, b, c

print(ares, bres, cres)