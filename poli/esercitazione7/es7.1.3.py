from random import randint


def remove_min(l):
    min = l[0]
    l.pop([(i, min := e) for i, e in enumerate(l) if e <= min][-1][0])


v = [randint(10, 100) for i in range(11)]

print("Lista:\t\t\t", *v)

remove_min(v)

print("Lista senza minimo:\t", *v)
