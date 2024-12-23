for _ in range(int(input())):
    len_n, n = int(input()), [int(x) for x in input().split()]
    res, sum, largest = 0, 0, 0

    # My previous attempt ignored completely the `largest` variable and thought it was simply a prefix problem.
    for a in n:
        sum += a
        largest = max(largest, a)
        if sum-largest == largest: res += 1

    print(res)
