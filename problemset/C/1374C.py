for _ in range(int(input())):
    _, parenthesis = input(), input()
    res, b = 0, 0
    for p in parenthesis:
        if p=='(': b += 1
        else:
            b -= 1
            if b < 0:
                b = 0
                res+=1
    print(res)
