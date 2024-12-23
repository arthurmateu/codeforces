_ = input("") # who cares
boxes = [str(x) for x in input("").split()]
boxes.sort(key=int)
print(" ".join(boxes))
