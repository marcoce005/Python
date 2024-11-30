def change_value(l):
    maximun = max([e[1] for e in l])
    for i in range(len(l)):
        l[i] = (l[i][0], round((l[i][1] * 40) / maximun))


l = []

nation = input("Inserire la nazione:\t")
n = input("Inserire un numero [positivo]:\t")
while n != "":
    l.append((nation, int(n)))
    nation = input("\nInserire la nazione:\t")
    n = input("Inserire un numero [positivo]:\t")

print("\n\nValori:\t", *l)

change_value(l)

print("Grafico\n")
[print(f"{e[0]:>15}:\t{"*" * e[1]}") for e in l]
