import math
""" 
    Abbiamo 20 metri di recinzione ed un lato gia' dato ed illimitato

    - Troviamo la combinazione che ci permette di avere il pollaio più grande possibile
"""

recinzione = 20

""" 
    Area del rettangolo == Lato1 * Lato2
"""
risultati = []
for i in range(0, int((recinzione / 2) + 1)):      # i --> rappresenta la somma dei lati più corti --> max == (20 / 2)
    A = abs(recinzione - (i * 2)) * i     # --> A = | lato_lungo | * lato_corto
    risultati.append(A)

print("Area massima possibile = ", max(risultati))