d, sumTime = (int(x) for x in input().split())
min_time, max_time = [], []

for _ in range(d):
    a, b = (int(x) for x in input().split())
    min_time.append(a)
    max_time.append(b)

if not sum(min_time) <= sumTime <= sum(max_time): 
    print("NO")
else:
    print("YES")
    
    extra = sumTime - sum(min_time)
    res = min_time[:]
    
    for i in range(d):
        cur = min(max_time[i] - min_time[i], extra)
        res[i] += cur
        extra -= cur

        if extra==0: break

    print(' '.join(str(x) for x in res))
