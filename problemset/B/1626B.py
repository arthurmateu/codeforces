# Original solution below. Didn't work exactly, so I ended up using the tutorial for help.
#t = int(input())
#for _ in range(t):
#    x = input()
#    last_two = sum(int(y) for y in x[-2:])
#    print(x[:-2]+str(last_two))

for _ in range(int(input())):
  x = [ord(c) - ord('0') for c in input()]
  n = len(x)
  for i in range(n - 2, -1, -1):
    if x[i] + x[i + 1] >= 10:
      x[i + 1] += x[i] - 10
      x[i] = 1
      break
  else:
    x[1] += x[0]
    x.pop(0)
  print(''.join([chr(c + ord('0')) for c in x]))
