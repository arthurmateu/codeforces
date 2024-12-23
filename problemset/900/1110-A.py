b, _ = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

if b%2==0:
    print("even" if a[-1]%2==0 else "odd")
else:
    print("even" if sum(1 for x in a if x%2==1)%2==0 else "odd")
