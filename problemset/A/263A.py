grid = [[i for i in input().split()] for _ in range(5)]
row, col = 0, 0
for r in range(5):
    for c in range(5):
        if grid[r][c] == '1':
            row, col = r, c
            break
print(abs(2-row)+abs(2-col))
