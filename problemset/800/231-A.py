# basically add to res if theres at least two `1's` in the line
res = 0
exercises = int(input(""))
for i in range(exercises):
    add = [int(x) for x in input("").split()]
    if sum(add) >= 2: res += 1
print(res)
