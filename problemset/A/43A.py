n = int(input())
res = []
for _ in range(n): res.append(input())
print(max(res, key=res.count))
