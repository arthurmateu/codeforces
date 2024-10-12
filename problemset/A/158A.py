n, k = (int(x) for x in input("").split())

contestants = [int(x) for x in input("").split()]
contestants.sort(reverse=True)

res, cutoff = 0, contestants[k-1]

for i in range(n):
    if contestants[i] > 0 and contestants[i] >= cutoff: res += 1
    else: break

print(res)
