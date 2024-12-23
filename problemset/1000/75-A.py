def remover(n):
    new = ""
    for ch in n:
        if ch=='0': continue
        new += ch
    return int(new)

a, b = input(), input()

c=str(int(a)+int(b))

print("YES" if remover(a)+remover(b)==remover(c) else "NO")
