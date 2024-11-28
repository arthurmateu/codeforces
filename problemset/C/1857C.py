for _ in range(int(input())):
    n, b = int(input()), sorted([int(x) for x in input().split()])
    j = 0
    for i in range(n-1, 0, -1):
        print(b[j], end=' ')
        j+=i
    print(b[-1])
