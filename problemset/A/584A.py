n, t = (int(x) for x in input().split())

if t == 10:
    if n == 1: print(-1)
    else: print('1' + '0'*(n-1))
else:
    smallest = 10**(n-1)

    if smallest%t==0: print(smallest)
    else: print(smallest+(t-smallest%t))
