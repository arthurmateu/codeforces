lines = int(input(""))
res = 0
for i in range(lines):
    cur =  input("")
    if cur == '++X' or cur == 'X++': res += 1
    else: res -= 1
print(res)
