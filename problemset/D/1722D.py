for _ in range(int(input())):
    n, a = int(input()), input()
    res, max_val = 0, []
    for i in range(n):
        if a[i] == 'L': 
            res += i
            max_val.append((n - i - 1) - i)
        else: 
            res += n - i - 1
            max_val.append(i - (n - 1 - i))
    max_val.sort(reverse=True)
    for i in range(n):
        res += max(0, max_val[i])
        print(res, end=' ')
    print()
