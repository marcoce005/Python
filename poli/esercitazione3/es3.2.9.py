wave_length = float(input("Inserire il valore della lunghezza d'onda in notazione esponenziale [1.23e4]:\t"))

C = 3e8

if wave_length <= 1e-11:
    print(f"{wave_length:.3e} --> Raggi gamma, f = {C / wave_length:.3e} hz")
elif wave_length <= 1e-8:
    print(f"{wave_length:.3e} --> Raggi X, f = {C / wave_length:.3e} hz")
elif wave_length <= 4e-7:
    print(f"{wave_length:.3e} --> Ultravioletti, f = {C / wave_length:.3e} hz")
elif wave_length <= 7e-7:
    print(f"{wave_length:.3e} --> Luce visibile, f = {C / wave_length:.3e} hz")
elif wave_length <= 1e-3:
    print(f"{wave_length:.3e} --> Infrarossi, f = {C / wave_length:.3e} hz")
elif wave_length <= 1e-1:
    print(f"{wave_length:.3e} --> Microonde, f = {C / wave_length:.3e} hz")
else:
    print(f"{wave_length:.3e} --> Onde radio, f = {C / wave_length:.3e} hz")
