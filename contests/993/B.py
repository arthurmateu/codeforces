for _ in range(int(input())):
    a, res = input(), ''
    for ch in reversed(a):
        if ch == 'q':
            res += 'p'
        elif ch == 'p':
            res += 'q'
        else:
            res += ch
    print(res)
