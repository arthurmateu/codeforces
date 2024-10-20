q = int(input())# testcases
cases = []

for _ in range(q):
    cases.append([int(x) for x in input().split()])

for i in range(q):
    a, b, n, s = cases[i]

    if (s%n <= b) and ((a*n + b) >= s):
        print("YES")
    else:
        print("NO")
