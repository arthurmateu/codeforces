t = int(input())
test_cases = [input() for _ in range(t)]

for tc in test_cases:
    stack = []
    for c in tc:
        if c == 'A': stack.append(c)
        if c == 'B':
            if stack: stack.pop()
            else: stack.append(c)
    print(len(stack))
