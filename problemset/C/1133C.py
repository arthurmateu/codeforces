n = int(input())
a = [int(x) for x in input().split()]
a.sort()
res, l, r = 0, 0, 0

while r < n:
    if abs(a[r]-a[l]) <= 5: r += 1
    else: l += 1
    res = max(res, r-l)

print(res)
