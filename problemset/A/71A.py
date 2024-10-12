words = int(input(""))
res = []
for i in range(words):
    cur = input("")
    if len(cur) > 10:
        cur = cur[0] + str(len(cur) - 2) + cur[-1]
    res.append(cur)

for w in res:
    print(w)
