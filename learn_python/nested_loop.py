## nested loop == for nidificati per le matrici


righe = int (input ("inserire righe: \t"))           ## input iniziali righe colonne numeri ecc...
colonne = int (input ("inserire colonne:\t"))
simbolo = input ("inserire simbolo:\t")

for i in range(righe) :             ## scorre le righe
    for j in range(colonne) :           ## scorre le colonne
        print (simbolo, end="")     ## va a capo solo alla fine della riga
    print ()