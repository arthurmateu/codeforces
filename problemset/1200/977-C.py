# k elements being lte to x
n, k = (int(x) for x in input().split())
seq = [int(x) for x in input().split()]
seq.sort()

# resorted to some help, since original answer didnt really work
if k==0:
    if seq[0]>1: print(seq[0]-1)
    else: print(-1)
elif k==n: print(seq[-1])
elif seq[k-1]==seq[k]: print(-1)
else: print(seq[k-1])
