n = int(input())
res, cur = 0, 0
for _ in range(n):
    a, b = (int(x) for x in input().split())
    cur = cur - a + b
    res = max(res, cur)
print(res)
