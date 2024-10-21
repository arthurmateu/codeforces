t = int(input())
test_cases = []

for _ in range(t):
    test_cases.append([int(x) for x in input().split()])

for n, k in test_cases:
    if k**2 <= n and n%2 == k%2:
        print('YES')
    else:
        print('NO')
