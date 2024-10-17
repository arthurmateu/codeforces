# there is an order to the numbers being shown, and one isnt following along. print its index <-- i was insanely wrong. its just that one value is of different evenness compared to the rest of the inputed values

n = int(input(""))
nums = [int(x) for x in input("").split()]
evenness = {0:0, 1:0}

for i in range(3):
    evenness[ nums[i] % 2 ] += 1

if evenness[1] > 1:
    for i in range(n):
        if nums[i] % 2 == 0: 
            print(i+1)
            break
else:
    for i in range(n):
        if nums[i] % 2 == 1:
            print(i+1)
            break
