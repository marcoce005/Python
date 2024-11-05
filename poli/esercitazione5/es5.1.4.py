MAX_TICKETS_FOR_PERSON = 4

tickets = 10
count = 0
while tickets > 0:
    print(f"Biglietti disponibili: {tickets}")
    n = int(input("Puoi prendere massimo 4 biglietti:\t"))
    if n > 4 or tickets - n < 0:
        print("Non puoi prendere questa quantità di biglietti")
    else:
        tickets -= n
        count += 1

print(f"{count} persone hanno comprato i biglietti")
