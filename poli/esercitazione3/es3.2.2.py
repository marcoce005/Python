voto = input("Inserire il voto:\t")

voti = ["F", "D", "C", "B", "A"]

if voto in ["F+", "F-"] or not voto[0] in voti:
    print("Voto inesistente")
elif len(voto) == 2 and (voto[1] == "+" or voto[1] == "-"):
    print(f"{voto} --> 4.0") if voto == "A+" else print(f"{voto} --> {voti.index(voto[0]) + 0.3 if voto[1] == '+' else voti.index(voto[0]) - 0.3}")
else:
    print("Voto inesistente")
