A = float(input("Inserire il tasso di crescita delle prede:\t"))
B = float(input("Inserire il tasso di distribuzione delle prede da parte dei predatori:\t"))
C = float(input("Inserire il tasso di mortalità dei predatori:\t"))
D = float(input("Inserire il tasso di incremento dei predatori attraverso il consumo delle prede:\t"))
x = int(input("Inserire la numerosità iniziale delle prede [intero]:\t"))
y = int(input("Inserire la numerosità iniziale dei predatori [intero]:\t"))
iter = int(input("Inserire numero di periodi da simulare [intero]:\t"))

for i in range(iter):
    print(f"Periodo {i + 1}:\nPrede:\t{x}\nPredatori:\t{y}\n")
    x_n = x
    y_n = y
    x = x_n * (1 + A - (B * y_n))
    y = y_n * (1 - C + (D * x_n))
