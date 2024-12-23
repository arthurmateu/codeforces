for _ in range(int(input())):
    h, m = (int(x) for x in input().split())
    print(1440-(h*60+m))
