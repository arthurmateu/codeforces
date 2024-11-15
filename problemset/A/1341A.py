for _ in range(int(input())):
    n, a, b, c, d = (int(x) for x in input().split())
    min_rice, max_rice = n*(a-b), n*(a+b)
    min_bag, max_bag = c-d, c+d
    if max(min_rice, min_bag) <= min(max_rice, max_bag): print('Yes')
    else: print('No')
