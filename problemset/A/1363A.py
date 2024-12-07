for _ in range(int(input())):
    len_n, x = (int(x) for x in input().split())
    odds = sum(1 for a in input().split() if int(a)%2==1)
    evens = len_n - odds
    flag = False
    for i in range(1, odds+1, 2):
        if i > x: continue
        if x-i <= evens:
            flag = True
            break
    print("Yes" if flag else "No")
