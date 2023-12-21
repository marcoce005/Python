## return = ritornare valori da una funzione


def somma(a, b) :
    tot = a + b
    return tot

n1 = int(input("\nInserire il primo numero:\t"))
n2 = int(input("\nInserire il secondo numero:\t"))

print("\nLa somma e':\t", somma(n1, n2))