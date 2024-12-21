for _ in range(int(input())):
    a,b,c = (int(x) for x in input().split())
    print("+" if a + b == c else "-")
