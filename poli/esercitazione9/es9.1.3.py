def change_value(l):
    maximun = max(l)
    for i in range(len(l)):
        l[i] = round((l[i] * 40) / maximun)


l = []

n = input("Inserire un numero [positivo]:\t")
while n != "":
    l.append(int(n))
    n = input("Inserire un numero [positivo]:\t")

print("\n\nValori:\t", *l)

change_value(l)

print("Grafico\n")
[print("*" * e) for e in l]