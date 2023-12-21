## set = collezione non in ordine senza indice e senza duplicati

from turtle import pos


posate = {"forchetta", "coltello", "cucchiaio", "coltello"}
attrezzi = {"trapano", "cacciavite", "martello","coltello"}

posate.add("cucchiaino")   ## aggiungo un elemento
posate.remove("forchetta")      ## rimuovo un elemento
# posate.clear()   cancello tutto
#posate.update(attrezzi)                 ## aggiungo un altro set

cose = posate.union(attrezzi)       ## li unisco dentro un altro

for i in cose :       ## ogni volta che lo stampi camvia l'ordine casuale non mette duplicati
    print (i)

print ("\n\n")


print (posate.difference(attrezzi))         ## le differenze che ci sono l'un altro
print (posate.intersection(attrezzi))           ## quelli che hanno in comune