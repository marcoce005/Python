""" 
    Obbiettivo:
        Ottenera la scatola con il volume maggiore dato un foglio 40cm per 50cm.
        Quale il lato del quadrato che va rimmosso per ottenere il volume maggiore?

    Volume = base * altezza * profondita'
"""

base = 40
altezza = 50

risultati = {}
for x in range(0, int(((base / 2) + 1))):   # --> tutte le dimensioni che può assumere x
    V = (base - (2 * x)) * (altezza - (2 * x)) * x
    risultati[x] = V

print("Per ottenere il volume massimo, x deve essere = ", max(risultati, key=risultati.get))