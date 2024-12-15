for _ in range(int(input())):
    m, a, b, c = (int(x) for x in input().split())
    res = 0
    row = m
    m *= 2

    if b >= row: 
        res += row
        m -= row
    else: 
        res += b
        m -= b

    if a >= row:
        res += row
        m -= row
    else:
        res += a
        m -= a

    if m > 0:
        if c >= m:
            res += m
        else:
            res += c

    print(res)
