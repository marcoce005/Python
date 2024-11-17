def find_biggest_space(l):
    return

def add_car(l):
    find_biggest_space(l)


n = int(input("Inserire il numero di posti che ha la fila [intero]:\t"))

l = ["_" for _ in range(n)]

print("Parheggio\n", *l, sep=" ")

park = input("Inserire y/N per parcheggiare o meno una persona:\t") == "y"
while park:
    add_car(l)

    print("Parheggio\n", *l, sep=" ")

    park = input("Inserire y/N per parcheggiare o meno una persona:\t") == "y"
