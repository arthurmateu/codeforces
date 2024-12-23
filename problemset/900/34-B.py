_, m = (int(x) for x in input().split())
tvs = sorted([int(x) for x in input().split()])
res = 0
for i in range(m):
    res += -tvs[i] if tvs[i] < 0 else 0
print(res)
