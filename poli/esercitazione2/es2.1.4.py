# Pseudo-codice
"""
costo_auto_nuova = ...
km_anno = ...
costo_carburante = ...
km_al_litro = ...
rivendita = ...

costo = costo_auto_nuova + (km_anno / km_al_litro) * costo_carburante

"""

costo_auto_nuova = float(input("Costo auto nuova:\t"))
km_anno = float(input("Kilometri percorsi in un anno:\t"))
costo_carburante = float(input("Costo medio carburante al litro:\t"))
km_al_litro = float(input("Consumo medio del veicolo km/L:\t"))
rivendita = float(input("Possibile ricavo dalla vendita:\t"))

costo_totale = costo_auto_nuova + ((km_anno / km_al_litro) * costo_carburante)

print(f"Costo totale dell'auto:\t{costo_totale}\nPossibile ricavo alla vendita:\t{rivendita}")
