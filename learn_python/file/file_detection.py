## gestione dei file trovare un file

import os           ## importare la libreria  OS

path = "/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/test.txt"

if os.path.exists(path) :           ## verifica se quel percorso esiste o meno
    print ("\nIl file esiste!")
    if os.path.isfile(path) :           ## verifica se è un file o meno
        print ("\nE' un file!")
    elif os.path.isdir(path) :                  ## altrimenti veriica se è una cartellla
        print ("\nE' una cartella")

else :
    print ("\nIl file non esiste!")