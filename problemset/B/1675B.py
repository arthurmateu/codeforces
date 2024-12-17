for _ in range(int(input())):
    n_len, n = int(input()), [int(x) for x in input().split()]
    res = 0
    for i in range(n_len-2, -1, -1):
        while n[i] >= n[i+1] and n[i] > 0:
            n[i]//=2
            res += 1
        if n[i] == n[i+1]:
            res = -1
            break
    print(res)
