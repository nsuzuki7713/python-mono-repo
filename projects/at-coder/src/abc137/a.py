# https://atcoder.jp/contests/abc137/tasks/abc137_a
a, b = map(int, input().split())

print(max(a+b, a-b, a*b))