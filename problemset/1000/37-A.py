from typing import Counter

n = int(input())
ls = [int(x) for x in input().split()]

largest_height = max(Counter(ls).values())
total_towers = len(set(ls))

print(str(largest_height) + " " + str(total_towers))
