def stampa(l, codice, x):
    print ("\n\nIl bit di parita' pari e'", int(x), "e il codice finale e' --> ", end="")
    for i in range(l):
        print(codice[i], end="")
    print (int(x))

    print ("\n\nIl bit di parita' dispari e'", int(not(x)), "e il codice finale e' --> ", end="")
    for i in range(l):
        print(codice[i], end="")
    print (int(not (x))) 
    
def parita(l, codice, tot):
    if tot % 2 == 0:
        stampa(l, codice, 0)
    else:
        stampa(l, codice, 1)


l = input("\n\nInserisci la lunghezza del codice:\t")           #inserire un dato dall'utente
l = int (l)

codice = []     #array in python
tot = 0 

print("Inserire il codice")
for i in range(l):
    a = input("Inserisci bit:\t")       #variabile di appoggio
    a = int (a)                     # lo faccio int
    codice.append(a)                # lo inserisco nell'array
    tot += a                          #faccio la somma totale

parita(l, codice, tot)