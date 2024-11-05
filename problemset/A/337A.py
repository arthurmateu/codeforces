n, m = (int(x) for x in input().split())
puzzles = [int(x) for x in input().split()]
puzzles.sort()
res = float('inf')
for i in range(m-n+1):
    cur = puzzles[i+n-1] - puzzles[i]
    res = min(res, cur)
print(res)
