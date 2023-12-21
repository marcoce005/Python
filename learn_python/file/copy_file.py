## copyfile() = copiare il contenuto di un file

## copy() = copyfile() + modalità di autorizzazione + destinazione

## copy2() = copy() +  copia i metadati (tempi di creazione e modifiche)

import shutil

shutil.copyfile('/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/test.txt', '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/test.txt')       ## src, destination 

shutil.copy2('/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/test.txt', '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/file/copy_file.txt')       ## src, destination 