## si può fare sia con i file o con le cartelle

import os

path_file = '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/cancella.txt'
path_dir = '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/cancella'


try :
    os.remove(path_file)
    os.rmdir(path_dir)

except FileNotFoundError : 
    print (path_dir + "\tnon trovato")
except PermissionError :
    print ("\nNon puoi eliminare questa cosa")

else :
    print (path_dir + "\teliminato")
    print (path_file + "\teliminato")