## muovere un file da una locazione all'altra

## si può anche usare con altri file o cartelle 

import os

source = "/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/cartella"
destination = "/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/destination/cartella"

try :
    if os.path.exists(destination) :            ## verifico che il file non ci sia già
        print ("\nC'è già il file qui!!!")
    else :
        os.replace(source, destination)             ## sposto il file
        print ("\nFile" +source, "spostato")

except FileNotFoundError :                      ## se il file non esiste do' errore
    print ("\nFile " +source, "non trovato!!!")