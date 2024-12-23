import math
for _ in range(int(input())):
    x, y, k = (int(x) for x in input().split())
    # To avoid importing the math module, each math.ceil could be instead written as:
    #       (x + k-1) // k
    print(max(math.ceil(x/k)*2-1, math.ceil(y/k)*2))
