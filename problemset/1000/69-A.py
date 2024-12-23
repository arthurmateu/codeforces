n = int(input())
x, y, z = 0, 0, 0
for _ in range(n):
    cur_x, cur_y, cur_z = (int(a) for a in input().split())
    x += cur_x
    y += cur_y
    z += cur_z

if (x, y, z) == (0, 0, 0): print("YES")
else: print("NO")
