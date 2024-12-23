for _ in range(int(input())):
    n_len, n = int(input()), [int(x) for x in input().split()]
    res = 0
    for i in range(1, n_len):
        res = max(res, n[i]*n[i-1])
    print(res)
