# https://atcoder.jp/contests/past201912-open/tasks/past201912_f

S = input()

words = []

i = 0
while i < len(S):

  # 単語の終わりの大文字を探す
  j = i + 1
  while j < len(S) and S[j].islower():
    j += 1
  
  words.append(S[i:j + 1])

  i = j + 1

words.sort(key=str.lower)

print("".join(words))