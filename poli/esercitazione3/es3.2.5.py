mark = float(input("Inserire il voto:\t"))

marks = ["F", "D", "C", "B", "A"]

if mark >= 0 and mark <= 4:
    decimal = round(mark % 1, 3)
    print(marks[int(mark) + 1] if round(decimal) else marks[int(mark)], end="")
    if decimal != 0 and decimal > 0.5:
        print("+" if decimal >= 0.3 and decimal <= 0.5 else "", end="")
        print("-" if decimal > 0.5 and decimal < 0.85 else "")
else:
    print("Voto non valido, compreso tra 0 e 4")
