fout = open('./chapter14/oops.txt', 'w')
print("Oops, I created a file.", file=fout)
fout.close()

fin = open('./chapter14/oops.txt', 'r')
text = fin.read()
fin.close()
print(text)