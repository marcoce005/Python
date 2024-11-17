from random import randint


def sum_without_smallest(v):
    return sum([e for e in v if e != min(v)])


v = [randint(0, 20) for _ in range(10)]

print("Lista:\t", *v)
print(f"Somma elementi senza minimo {min(v)} = {sum_without_smallest(v)}")
