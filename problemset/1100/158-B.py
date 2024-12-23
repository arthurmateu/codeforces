from collections import Counter


n = int(input(''))
groups = [int(x) for x in input('').split()]

res = 0
counter = Counter(groups)

res += counter[4] + counter[3] + counter[2]//2
counter[1] = max(0, counter[1]-counter[3])
if counter[2] % 2 == 1:
    res += 1
    counter[1] = max(0, counter[1]-2)
res += (counter[1]+3)//4

print(res)
