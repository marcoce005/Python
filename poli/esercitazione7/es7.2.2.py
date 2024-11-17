def find_biggest_space(l):
    biggest = max("".join(l).split("X"))
    index_biggest = "".join(l).index(biggest)

    return index_biggest, len(biggest)


def add_car(l):
    index = find_biggest_space(l)

    l[(index[1] // 2) + index[0]] = "X"


n = int(input("Inserire il numero di posti che ha la fila [intero]:\t"))

l = ["_"] * n

print("Parheggio\n", *l, sep=" ")

park = input("Inserire y/N per parcheggiare o meno una persona:\t") == "y"
while park and l != ["X"] * n:
    add_car(l)

    print("Parheggio\n", *l, sep=" ")

    park = input("Inserire y/N per parcheggiare o meno una persona:\t") == "y"
