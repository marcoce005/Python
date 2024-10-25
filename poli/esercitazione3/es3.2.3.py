month = int(input("Inserire il mese come numero intero [iniziare da 1]:\t"))
gg = int(input("Inserire il giorno come numero intero:\t"))

if month > 0 and month < 13 and gg > 0 and gg < 32:
    if month < 4:
        season = "Winter"
    elif month < 7:
        season = "Spring"
    elif month < 10:
        season = "Summer"
    else:
        season = "Fall"

    if month % 3 == 0 and gg >= 21:
        if season == "Winter":
            season = "Fall"
        elif season == "Spring":
            season = "Summer"
        elif season == "Summer":
            season = "Fall"
        else:
            season = "Winter"

    print(f"{month}/{gg} --> {season}")
else:
    print("mese o giorno non esistente")
