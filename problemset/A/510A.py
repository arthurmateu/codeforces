n, m = (int(x) for x in input().split())
cur = 0
for i in range(n):
    if i%2==0:
        line = '#' * m
        print(line)
    else:
        line = '.' * (m-1)
        if cur%2==0:
            line = line + '#'
        else: 
            line = '#' + line
        cur += 1
        print(line)
