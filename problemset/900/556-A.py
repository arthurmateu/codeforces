_, x = input(), input()
stack = []

for ch in x:
    if stack and stack[-1] != ch: stack.pop()
    else: stack.append(ch)

print(len(stack))
