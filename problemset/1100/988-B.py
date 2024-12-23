s = []
for _ in range(int(input())):
    s.append(input())
ss = sorted(s, key=len)
flag = True
for i in range(1, len(ss)):
    if ss[i-1] not in ss[i]:
        flag = False
        break
if flag:
    print("YES")
    for w in ss: print(w)
else:
    print("NO")
