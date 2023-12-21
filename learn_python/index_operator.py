## index operator [] = da l'accesso a una sequenza di elementi (stringhe, liste, tuples, ecc...)


name = "pippo Pluto&"

if (name[0].islower()) :            ## verifica se la prima lettere e maiuscola o minuscola
    name = name.capitalize()            ## diventa maiuscola
else :
    name = name.casefold()      ## diventa minuscola

print (name, "\n\n")

first_name = name[0 : 5].upper()        ## seleziona il primo nome e lo fa maiuscolo        (è indiferrente mettere [0 : 5] o [: 5])
print (first_name)

second_name = name[6 :].lower()     ## seleziona il secondo nome e lo fa minuscolo
print (second_name)

ultimo_carattere = name[-1]     ## gli indici negativi vuol dire che parte da dx verso sx
print (ultimo_carattere)