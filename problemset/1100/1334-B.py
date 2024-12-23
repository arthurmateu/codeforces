for _ in range(int(input())):
    len_n, x = (int(x) for x in input().split())
    n = sorted([int(x) for x in input().split()])

    i, subset_sum = 0, sum(n)
    while i < len_n and subset_sum/(len_n-i) < x:
        subset_sum -= n[i]
        i += 1

    print(len_n - i)
