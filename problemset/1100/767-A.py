import heapq

n = int(input())
order = [int(x) for x in input().split()]

wait, l = n, []
for i in reversed(range(1, n+1)):
    heapq.heappush(l, -order[n-i])
    if wait == -l[0]:
        while l and -l[0] == wait:
            print(-heapq.heappop(l), end=" ")
            wait -= 1
    print()
