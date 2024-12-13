for _ in range(int(input())):
    n = int(input())
    res = (n*(1+n))//2
    power, take = 1, 0
    while power <= n:
        take += power
        power *= 2
    print(res-(take*2)) # take once would just skip them, twice actually takes them
