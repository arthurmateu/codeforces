from typing import Counter


for _ in range(int(input())):
    points = []
    for _ in range((n:=int(input()))):
        x,y = (int(x) for x in input().split()) # I tried putting this inside the append function but it didn't work somehow
        points.append((x,y))

    res = 0
    # There has to be a line (x1==x2 or y1==y2) and another element that shares x (if y1==y2) or y (if x1==x2) with another one of the points
    # After this point, I got a bit stuck so I've read the tutorial
    b, check = Counter(x for (x, _) in points),  set(points)

    for i in b:
        if b[i] == 2:
            res += n-2

    for (x, y) in check:
        if (x-1, y^1) in check and (x+1, y^1) in check:
            res += 1

    print(res)
