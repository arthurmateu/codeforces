# n -> how many rides she needs to do
# m -> [special] rides pert ticket
# a -> ticket cost
# b -> [special] ticket cost

n, m, a, b = (int(x) for x in input().split())

single = n * a
special = ((n + m - 1) // m) * b
mixed = (n // m) * b + (n % m) * a 

print(min(single, special, mixed))
