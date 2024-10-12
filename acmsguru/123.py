S = int(input())
fib = [1, 1]
for i in range(2, S):
    fib.append(fib[i-1] + fib[i-2])
print(sum(fib))
