for _ in range(int(input())):
    # my original answer where i just multiply the input by 10/9 didn't work
    s, res = int(input()), 0
    pw = 1000 * 1000 * 1000
    while s > 0:
        while s < pw:
            pw //= 10
        res += pw
        s -= pw - pw // 10
    print(res)
