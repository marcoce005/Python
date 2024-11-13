from math import pi


def diameter(wire_gauge):
    return 0.127 * (92 ** ((36 - wire_gauge) / 39))


def copper_wire_resistance(length, wire_gauge):
    P = 1.678e-8
    return (4 * P * length) / (pi * ((diameter(wire_gauge) / 1000) ** 2))


def aluminum_wire_resistance(length, wire_gauge):
    P = 2.82e-8
    return (4 * P * length) / (pi * ((diameter(wire_gauge) / 1000) ** 2))


w_g = int(input("Inserire il calibro americano AWG [intero]:\t"))
a_or_c = bool(int(input("Inserire il materiale del cavo [0 --> rame, 1 --> alluminio]:\t")))
l = float(input("Inserire la lunghezza del cavo [m]:\t"))

print(f"\n\nDiametro:\t{diameter(w_g):.2f} mm")
print(
    f"\nResistività cavo di {'alluminio' if a_or_c else 'rame'} di {l} m:\t{aluminum_wire_resistance(l, w_g) if a_or_c else copper_wire_resistance(l, w_g):.2e} hom"
)
