w = input("")

if w.isupper():
    print(w.lower())
elif all(c.isupper() for c in w[1:]):
    print(w.title())
else:
    print(w)
