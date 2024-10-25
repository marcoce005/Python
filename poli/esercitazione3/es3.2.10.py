v = float(input("Inserire la velocità di salto [in km/h]:\t"))

G = 6.67e-11
M = 2.2e14
R = 9400 / 2

v_escape = ((2 * G * M) / R) ** 0.5

if v < 0:
    print("velocità errata")
else:
    print(f"Volerai via\nPer riatterrare sulla cometa la massa di quest'ultima dovrebbe essere {(((v / 3.6) ** 2) * R) / (2 * G):.3e} kg") if v > v_escape * 3.6 else print("Riatterrerai sulla cometa")
