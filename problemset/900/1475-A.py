n = int(input(""))
nums = []
for _ in range(n):
    nums.append(int(input("")))

for num in nums:
    while num % 2 == 0: num //= 2
    if num == 1:
        print("NO")
    else:
        print("YES")
