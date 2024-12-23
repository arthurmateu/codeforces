# n -> number of coins
# afterwards, the value of said coins

n = int(input(""))
coins = [int(x) for x in input("").split()]
coins.sort()

# value taken > sum(coins) / 2, BUT lowest number of coins
reach = sum(coins)/2
value = 0
res = 0

for i in range(len(coins)-1, -1, -1):
    value += coins[i]
    res += 1
    if value > reach:
        break
print(res)
