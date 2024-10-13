# first will be all odds from 1 to n, then all evens
import math # my original solution was O(n) and it obviously didnt work.

n, k = (int(x) for x in input("").split())
res, mid = 0, math.ceil(n/2)
if k <= mid:
    res = (2 * k) - 1
else:
    res = (k - mid) * 2
print(res)
