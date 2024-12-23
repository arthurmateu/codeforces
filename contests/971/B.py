for _ in range(int(input())):
    res = []
    for _ in range(int(input())):
        res.append(str(input().find('#')+1))
    print(' '.join(reversed(res)))
