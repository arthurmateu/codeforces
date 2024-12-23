n = int(input())
res = ""
for i in range(n):
    if i % 2 == 0:
        res += " I hate that"
    else:
        res += " I love that"

print( res[1:-4] + "it" )
