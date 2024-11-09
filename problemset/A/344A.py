n = int(input())
res, last = 0, ''
for _ in range(n):
    cur = input()
    if cur != last:
        res += 1
        last = cur
print(res)
