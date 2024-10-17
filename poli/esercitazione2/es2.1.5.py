from math import pi

EPSILON = 8.854E-12

q1 = float(input("Carica 1, Q1 = "))
q2 = float(input("Carica 2, Q2 = "))
r = float(input("Raggio, r = "))

print(f"Forza elettrica = {(q1 * q2) / (4 * pi * EPSILON * (r ** 2))}")
