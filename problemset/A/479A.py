a, b, c = int(input()), int(input()), int(input())
res = max(a+b+c, (a+b)*c, a*(b+c), a*b*c)
print(res)
