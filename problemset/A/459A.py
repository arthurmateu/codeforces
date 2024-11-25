x1, y1, x2, y2 = (int(x) for x in input().split())

# had to read the tutorial
if x1 == x2:
    a = abs(y2-y1)
    print(x1+a, y1, x2+a, y2)
elif y1 == y2:
    a = abs(x2-x1)
    print(x1, y1+a, x2, y2+a)
elif abs(x2-x1) == abs(y2-y1):
    print(x1, y2, x2, y1)
else:
    print(-1)

