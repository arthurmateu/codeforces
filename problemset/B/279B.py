# n -> number of books
# t -> free minutes
n, t = (int(x) for x in input("").split())
books = [int(x) for x in input("").split()]

l =  0
cur, res = 0, 0
for r in range(n):
    cur += books[r]
    while cur > t:
        cur -= books[l]
        l += 1
    res = max(res, r-l+1)
print(res)
