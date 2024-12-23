# if word input has more than half the letters as uppercase, print upper
# else, print lower
w = input()
res = 0
for c in w:
    if c.isupper(): res += 1
if res > len(w)//2: print(w.upper())
else: print(w.lower())
