## scrivere su un file .txt

                ## come in C:  r leggi; w scrivi; a crei o aggiungi un pezzo

text = "\nHello,  ciao sono pippo!!!!"

try :
    with open ('/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/test.txt', 'a') as file : 
        file.write(text)
    
except FileExistsError :
    print ("\nIl file non esiste!")