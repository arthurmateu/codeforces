from typing import Counter


n = []
for _ in range(int(input())):
    h, m = (int(x) for x in input().split())
    n.append(h*60+m)
print(max(Counter(n).values()))
