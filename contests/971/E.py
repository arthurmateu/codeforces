# Understood the general idea of this exercise, but couldn't really understand how to implement it
def val(m):
    v1 = (m+k-1+k)*m//2
    v2 = (k+n-1+k)*n//2 - v1
    return v1, v2


for _ in range(int(input())):
    # [k -> k + n-1]
    n, k = (int(x) for x in input().split())
    res, l, r = 1, 1, n
    while l <= r:
        m = (l+r)//2
        a, b = val(m)
        if b > a:
            res = m
            l = m+1
        else:
            r = m-1

    a1, b1 = val(res)
    a2, b2 = val(res+1)

    print(min(b1-a1, a2-b2))

# There was also a F problem, but I didn't do it because the editorial only shows C++ solutions (and there wasn't apparently a Python solution that could pass given the time-constraints).
# Guess I'll have to learn some C++ or something
