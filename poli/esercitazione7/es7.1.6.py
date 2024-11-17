from random import randint

l = [randint(0, 99) for _ in range(20)]

print("Lista:\t", *l)

l.sort()

print("Lista:\t", *l)
