name = "pippo casa"

l = len(name)       ##lunghezza
print(l)

n = name.find("p")          ##trova una lettera / parola
print(n)

print(name.capitalize())        ##mette la la prima lettera maiuscola le altre tutte minuscole
print(name.upper())         ##maiuscolo upper minuscolo lower

print(name.isalpha())           ##vedere se ci sono spazi
print(name.count("p"))          ##contare un carattere

print(name.replace("p", "f"))      ## cambiare della lettere/parole

print(name*3)       ##stampa n volte 