# https://atcoder.jp/contests/abc104/tasks/abc104_b

def isAC(S):
  if S[0] != "A":
    return False
  
  if S[2:-1].count("C") != 1:
    return False
  
  # Sに含まれている大文字の工数を調べる
  if sum(map(str.isupper, S)) != 2:
    return False
  
  return True

S = input()

print("AC" if isAC(S) else "WA")
