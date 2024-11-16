from random import randint, random


def filter(l, func):
    return [e for i, e in enumerate(l) if func(i, e)]


l = [randint(10, 100) for i in range(11)]

print("Lista:\t", *l)

print("Indici pari:\t", *filter(l, lambda i, e: i % 2 == 0))

print("Valore pari:\t", *filter(l, lambda i, e: e % 2 == 0))

print("Ordine inverso:\t", *reversed(l))
