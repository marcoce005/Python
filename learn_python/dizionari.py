## dizionari = modificabili collezione non ordinata; si orienta in base alla parola chiave iniziale
##              veloce perche usa hashing per accedere ai 'value'

from multiprocessing.sharedctypes import Value
from xml.sax.saxutils import prepare_input_source


capitali = {'USA' : 'Washinton DC',
            'Italy' : 'Rome', 
            'UK' : 'London', 
            'France' : 'Paris'}

print (capitali['Italy'])       ## in base alla parola chiave stampa il suo risultato
print (capitali.get('Germany'))         ## non trova quella parola chiave
print (capitali.keys())         ## stampa tutte le chiavi
print (capitali.values())               ## stampa tutti i valori associati alle chiavi
print (capitali.items(), "\n\n")            ## stampa tutti gli accoppiamenti

capitali.update({'Germany' : 'Berlin'})    ## per aggiungere o modificare delle chiavi al dizionario
capitali.update({'USA' : 'New York'})

capitali.pop('France')      ## per eliminare una chiave e annessa parola
#capitali.clear()        ## cancellare tutto il dizionario

for key, value in capitali.items() :
    print (key, value)                  ## stampare chiavi e parole

