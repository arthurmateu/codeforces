n = int(input())
s = input()

removals, stack = 0, []
for ch in s:
    if len(stack)%2==0 or stack[-1] != ch:
        stack.append(ch)

if len(stack)%2==1: stack.pop()
print(n - len(stack))
print(''.join(stack))
