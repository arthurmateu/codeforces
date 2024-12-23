for _ in range(int(input())):
    x, y = (int(x) for x in input().split())
    a, b = (int(x) for x in input().split())
    b = min(b, a+a)
    if x < y:
        x, y = y, x
    print(y * b + (x-y) * a)
