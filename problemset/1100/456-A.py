laptops, n = [], int(input())
for _ in range(n):
    laptops.append([int(x) for x in input().split()]) # price and quality 
laptops.sort()
res = "Poor"
for i in range(1, n):
    if laptops[i-1][1] > laptops[i][1]:
        res = "Happy"
        break
print(res + " Alex")
