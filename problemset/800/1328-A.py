t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append((int(x) for x in input().split()))

for a, b in test_cases:
    if a % b == 0: print(0)
    else: print(b - a%b)
