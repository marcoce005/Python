A = 32310901
B = 1729
M = 2e24

r_old = int(input("Inserire il valore iniziale [intero]:\t"))

for i in range(100):
    r_new = ((A * r_old) + B) % M
    print(r_new)
    r_old = r_new
