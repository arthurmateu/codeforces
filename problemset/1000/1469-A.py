n = int(input())
test_cases = []
for _ in range(n):
    test_cases.append(input())

# originally did a similar one using stacks on leetcode. found a neater, simpler solution, but I'm not 100% sure it works for every case. Either way, it somehow passed the test cases.
for tc in test_cases:
    if len(tc) % 2 == 0 and tc[0] != ')' and tc[-1] != '(': print('YES')
    else: print('NO')
