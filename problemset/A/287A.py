matrix = [input().strip() for _ in range(4)]

def check(r, c):
    square = [matrix[r][c], matrix[r+1][c], matrix[r][c+1], matrix[r+1][c+1]]
    return square.count('#') >= 3 or square.count('.') >= 3

valid = False
for r in range(3):
    for c in range(3):
        if check(r,c): valid = True

print("YES" if valid else "NO")
