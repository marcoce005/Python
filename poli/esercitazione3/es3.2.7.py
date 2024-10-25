unit_start = input("Scegliere l'unità di partenza [opzioni:  ml, l, g, kg, mm, cm, m, km]:\t")
value = float(input("Inserire valore:\t"))
unit_end = input("Scegliere l'unità di arrivo [opzioni: fl, oz, gal, lb, in, ft, mi]:\t")

volume = ["ml", "l", "gal", "fl"]
mass = ["g", "kg", "oz", "lb"]
distance = ["mm", "m", "cm", "km", "in", "ft", "mi"]

all_unit = [*volume, *mass, *distance]

if unit_start and unit_start in all_unit:
    if unit_start and unit_end in volume:
        if unit_start == "l" and unit_end == "gal":
            print(f"{value} l --> {value / 3.785:.5f} gal")
        elif unit_start == "l" and unit_end == "fl":
            print(f"{value} l --> {(value / 3.785) / 128:.5f} fl")
        elif unit_end == "gal":
            print(f"{value} ml --> {(value / 3785):.5f} gal")
        elif unit_end == "fl":
            print(f"{value} ml --> {(value / 29.574):.5f} fl")
        else:
            print("conversione non supportata")
    elif unit_start and unit_end in mass:
        if unit_start == "g" and unit_end == "oz":
            print(f"{value} g --> {value / 28.35:.5f} oz")
        elif unit_start == "g" and unit_end == "lb":
            print(f"{value} g --> {value / 453.6:.5f} lb")
        elif unit_end == "oz":
            print(f"{value} kg --> {value * 35.274:.5f} oz")
        elif unit_end == "lb":
            print(f"{value} kg --> {value * 2.205:.5f} lb")
        else:
            print("conversione non supportata")
    elif unit_start and unit_end in distance:
        if unit_start == "cm" and unit_end == "in":
            print(f"{value} cm --> {value / 2.54:.5f} in")
        elif unit_start == "cm" and unit_end == "ft":
            print(f"{value} cm --> {value / 30.48:.5f} ft")
        elif unit_start == "cm" and unit_end == "mi":
            print(f"{value} cm --> {value / 160900:.8f} mi")
        elif unit_start == "mm" and unit_end == "in":
            print(f"{value} mm --> {(value / 10) / 2.54:.5f} in")
        elif unit_start == "mm" and unit_end == "ft":
            print(f"{value} mm --> {(value / 10) / 30.48:.5f} ft")
        elif unit_start == "mm" and unit_end == "mi":
            print(f"{value} mm --> {(value / 10) / 160900:.8f} mi")
        elif unit_start == "m" and unit_end == "in":
            print(f"{value} m --> {(value * 100) / 2.54:.5f} in")
        elif unit_start == "m" and unit_end == "ft":
            print(f"{value} m --> {(value * 100) / 30.48:.5f} ft")
        elif unit_start == "m" and unit_end == "mi":
            print(f"{value} m --> {(value * 100) / 160900:.8f} mi")
        elif unit_end == "in":
             print(f"{value} km --> {(value * 100000) / 2.54:.5f} in")
        elif unit_end == "ft":
            print(f"{value} km --> {(value * 100000) / 30.48:.5f} ft")
        elif unit_end == "mi":
            print(f"{value} km --> {(value) / 1.609:.8f} mi")
        else:
            print("conversione non supportata")
    else:
        print("Conversione impossibile")
else:
    print("Dati errati")
