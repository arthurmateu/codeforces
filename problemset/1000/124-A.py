n, a, b = (int(x) for x in input().split())
print(n-max(a+1, n-b)+1) # thought it was n-a+b initially
