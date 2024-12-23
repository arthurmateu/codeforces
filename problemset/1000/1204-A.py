n = int(input(), 2)
trains, t = 0, 1
while t < n:
    trains += 1
    t *= 4
print(trains)
