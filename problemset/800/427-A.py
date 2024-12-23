_ = input() # who cares
cases = [int(x) for x in input().split()]

police = 0
res = 0

for c in cases:
    if c > 0: 
        police += c
    else:
        if police:
            police -= 1
        else:
            res += 1

print(res)
