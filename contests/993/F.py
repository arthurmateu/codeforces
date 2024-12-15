n, m, q = (int(x) for x in input().split())
n_vals = [int(x) for x in input().split()]
m_vals = [int(x) for x in input().split()]

grid = [[0]*n for _ in range(m)]
for r in range(n):
    for c in range(m):
        grid[r][c] = n_vals[r] * m_vals[c]

row_sums = [sum(row) for row in grid]
col_sums = [sum(col) for col in zip(*grid)]
total = sum(row_sums+col_sums)

# precompute every single possible beauty score
beauty = [[0]*n for _ in range(m)]
for r in range(n):
    for c in range(m):
        beauty[r][c] = total - row_sums[r] - col_sums[c] + grid[r][c] # adding it once to avoid removing it twice

flattened = []
for row in beauty:
    flattened.extend(row)

for _ in range(q):
    print("YES" if int(input()) in flattened else "NO")
