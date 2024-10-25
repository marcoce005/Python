prize = float(input("Inserire importo dello scontrino:\t"))

if prize <= 0:
    print("Spesa non valida o insufficiente")
elif prize <= 10:
    print("Mi dispiace ma lei non ha diritto a nessun buono")
elif prize <= 60:
    print(f"Con una spesa di {prize} $ ha ottenuto {prize * 0.08:.2f} $ di buono sconto")
elif prize <= 150:
    print(f"Con una spesa di {prize} $ ha ottenuto {prize * 0.1:.2f} $ di buono sconto")
elif prize <= 210:
    print(f"Con una spesa di {prize} $ ha ottenuto {prize * 0.12:.2f} $ di buono sconto")
else:
    print(f"Con una spesa di {prize} $ ha ottenuto {prize * 0.14:.2:.2ff} $ di buono sconto")
