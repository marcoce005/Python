## leggere da un file .txt

try :
    with open ('/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/test.txt') as file : 
        print (file.read())
    
except FileExistsError :
    print ("\nIl file non esiste!")