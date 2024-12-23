drinks = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
res = 0

for _ in range(int(input())):
    w = input()
    if (w.isnumeric() and int(w) < 18) or w in drinks: res += 1

print(res)
