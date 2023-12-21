## liste == array / vettori

cibi = ["pasta", "pizza", "carne", "frutta"]                ## un array / vettore di stringhe
print (cibi)        ## stampa tutto il vettore / array
print (cibi[1])             ## stampa solo la locazione 1 del vettore / array

print ("\n\n")

cibi[1] = "cavolo"          ## modifico la locazione 1 con un'altra parola
print (cibi[1])

print ("\n\n")

cibi.pop()      ## rimuove l'ultimo elementode dell'array
cibi.append("mela")     ## aggiungo un elemento all'array
cibi.remove("carne")     ## rimuovo un elemento all'array
cibi.insert(2, "torta")         ## inserisco un elemento dove voglio gli altri scalano 
cibi.sort()         ## riordina in ordine alfabetico
cibi.clear()            ## rimuove tutti gli elementi dall'array 


for i in cibi :        ## scorro il vettore / array per la sua lnghezza 
    print (i)