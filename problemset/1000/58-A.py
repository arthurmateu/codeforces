s = input()
res = 0 # initially thought of stacks but this seemed easier and less memory consuming
for c in s:
    # yes im well aware these if statements look hideous. tough luck.
    if res == 0 and c == 'h': res += 1
    elif res == 1 and c == 'e': res += 1
    elif (res == 2 or res == 3) and c == 'l': res += 1
    elif res == 4 and c == 'o': res += 1

    if res == 5: break

print("YES" if res == 5 else "NO")
