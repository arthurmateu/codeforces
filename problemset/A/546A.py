# k -> dollars/cost/result
# n -> how many dollars he has
# w -> bananas
k, n, w = (int(x) for x in input().split())
res = 0
for i in range(1, w+1):
    res += k*i
if n >= res: 
    print(0)
else:
    print(res - n)
