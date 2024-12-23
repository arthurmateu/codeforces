word = input("")
res = ""
for w in word.split("WUB"):
    if not w: continue
    res += w + " "
print(res[:-1])
