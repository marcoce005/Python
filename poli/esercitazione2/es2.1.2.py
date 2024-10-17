try:
    r1 = float(input("R1 = "))
    r2 = float(input("R2 = "))
    r3 = float(input("R3 = "))
except:
    print("Errore nell'inserirmento dei dati")

print(f"R totale = {r1 + (1 /((1 / r2) + (1 / r3)))}")
