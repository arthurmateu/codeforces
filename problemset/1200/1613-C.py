for _ in range(int(input())):
    n, h = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]

    l, r, res = 1, h, h
    while l <= r:
        m, dealt = (l+r)//2, 0
        for i in range(n-1):
            dealt += min(m, a[i+1]-a[i])
        dealt += m

        if dealt >= h:
            res = m
            r = m-1
        else: l = m+1

    print(res)
