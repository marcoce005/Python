## il valore di una variabile dipende da dove si trova


name = "pluto"          ## variabile globale (vale in tutto il programma)

def stampa() :
    name = "pippo"      ## variabile locale (solo nella funzione)
    print (name)

print (name)
stampa()