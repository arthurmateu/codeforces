x1 = input()
x2 = input()
res = ""
for i in range(len(x1)):
    if (x1[i] == '0' and x2[i] == '1') or (x1[i] == '1' and x2[i] == '0'):
        res += '1'
    else:
        res += '0'
print(res)
