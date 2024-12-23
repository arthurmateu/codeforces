a, b = (int(x) for x in input().split())
res, leftover = 0, 0
while a > 0:
    res += a
    tmp = a + leftover
    a = tmp // b
    leftover = tmp % b
print(res)
