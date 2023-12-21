## tuple = simile ad un vettore ma è oridnato e non modificabile (forse +- una struttura)

studente = ["pippo", 23, "maschio"]

print (studente.count("pippo"))     ## conto quante volte la parola appare nel tuple

print ("\n\n")

print (studente.index("maschio"))           ## ti dice la locazione della parola

print ("\n\n")

for i in studente :
    print (i)

print ("\n\n")

if "pippo" in studente :
    print ("sono qui!!!")