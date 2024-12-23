x = list(input())
for i in range(len(x)):
    digit = int(x[i])
    if digit == 9 and i == 0: continue # edge case
    if digit > 4:
        x[i] = str(9 - digit)

print(''.join(x))
