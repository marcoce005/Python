P = 1.23
C_D = 0.2
A = 2.5


kmh_2_ms = lambda v: v / 3.6
# def kmh_2_ms(v):
#     return v / 3.6


resistence_force = lambda v: 0.5 * P * (kmh_2_ms(v) ** 2) * A * C_D
# def resistence_force(v):
#     return 0.5 * P * (kmh_2_ms(v) ** 2) * A * C_D


power = lambda v: resistence_force(v) * kmh_2_ms(v)
# def power(v):
#     return resistence_force(v) * v


horse_power = lambda v: power(v) / 745.7
# def horse_power(v):
#     return power(v) / 745.7


print(f"A 100 km/h\nCavalli:\t{horse_power(100):.1f} hp\nPotenza:\t{power(100):.1f} W")
