for _ in range(int(input())):
    rgb = sorted([int(x) for x in input().split()])
    print("Yes" if rgb[2] <= rgb[0]+rgb[1]+1 else "No") # i wasnt expecting the +1, but I got it almost completely identical to the editorial's answer
