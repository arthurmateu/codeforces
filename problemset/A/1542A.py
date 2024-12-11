for _ in range(int(input())):
    len_n, n = int(input()), [int(x) for x in input().split()]
    print("Yes" if sum(1 for x in n if x%2==1) == len_n else "No")
