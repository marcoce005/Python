## la formattazione delle stringhe serve per avere più controllo nella fase di output

animale = "mucca"
parola = "casa"

print ("La {} mangia la {}".format(animale, parola))

print ("La {1} mangia la {0}".format(animale, parola))      ## si può cambiare in base alla seguenza (si possono usare anche i nomi delle variabili)
print ("La {1} mangia la {1}".format(animale, parola))

testo = "La {} mangia la {}"
print (testo.format(animale, parola), "\n\n")

print ("Ciao, sono una {:10}hello".format(animale), "\n\n")         ## con i ':' si specifica quanto proseguire (deve essere > della parola messa)

print ("Ciao, sono una {:>20} hello".format(animale))        ## il nome va tutto a destra
print ("Ciao, sono una {:<20} hello".format(animale))        ## il nome va tutto a sinistra
print ("Ciao, sono una {:^20} hello".format(animale), "\n\n")        ## il nome sta in centro

numero = 3.67549373874
n2 = 4567890
n3 = 65

print ("Il numero e' {:.4f}".format (numero))       ## selezionare quanti numeri dopo la virgola
print ("Il numero e' {:,}".format (n2))         ## mette la virgola alle migliaia

print ("Il numero e' {:e}".format (n3))         ## converte in notazione esponenziale

print ("Il numero e' {:b}".format (n3))         ## converte in binario
print ("Il numero e' {:o}".format (n3))         ## converte in ottale
print ("Il numero e' {:x}".format (n3))         ## converte in esadecimale