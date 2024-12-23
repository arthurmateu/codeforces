for _ in range(int(input())):
    l, r, d = (int(x) for x in input().split())

    # previous answer with a while loop got time exceeded, didn't think about the purely-math solution
    print(d if d<l or d>r else (r//d)*d+d)
