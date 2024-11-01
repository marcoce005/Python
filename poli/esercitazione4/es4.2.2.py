from math import log, e

T = 6   # emivita del tecnezio-99

_lambda = log(2) / T

a_0 = float(input("Inserire la quantità di radiozioni assorbite:\t"))

for t in range(1, 25):
    a = a_0 * (e ** (- _lambda * t))
    print(f"{t:2d} h --> {(a / a_0) * 100:8.5f} %")
