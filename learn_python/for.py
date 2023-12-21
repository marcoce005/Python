## for

import time             ## importare libreria time per il tempo

for i in range(10) :            ## da 0 a 9 (<10)
    print (i)

print ("\n\n\n\n")

for j in range(10, 15) :            ## da 10 a 14
    print (j)


print ("\n\n\n\n")

for k in range(10, 17, 2) :            ## da 10 a 16 di due in due
    print (k)

print ("\n\n\n\n")

for p in "Ciruzzo":             ## stampa le lettere una sotto l'ratra
    print (p)

print ("\n\n\n\n")

for tempo in range (5, 0, -1):         ## conto alla rovescia reale
    print (tempo)
    time.sleep(1)