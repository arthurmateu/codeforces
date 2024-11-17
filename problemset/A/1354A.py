# used tutorial bc i didnt even manage to understand the problem completely
t = int(input())
for _ in range(t):
    a, b, c, d = (int(x) for x in input().split())
    if b >= a:
        print(b)
        continue
    if c <= d:
        print(-1)
        continue
    a -= b
    dif = c - d
    print(b+(a+dif-1)//dif*c)
