## break = per terminare il loop intero

## continue = per saltare la prossima azione del loop

## pass = per segnare il posto (non fa niente)


while True :
    name = input ("inserire il nome:\t")
    if name == "pippo" :
        break                       ## esce solo se è "pippo"

print ("\n\n\n\n")

telefono = "355-789-43-12"

for i in telefono :
    if i == "-" :
        continue                ## salta (non considera quel carattere)
    print (i, end="")

print ("\n\n\n\n")

for i in range(0, 10) :
    if i == 7 :
        pass            ## non fa niente 
    else :
        print (i)