# 7 of the same in a row
field = input("")
cur, res = 1, "NO"
for i in range(1, len(field)):
    if field[i] == field[i-1]: cur += 1
    else: cur = 1

    if cur == 7: 
        res = "YES"
        break
print(res)
