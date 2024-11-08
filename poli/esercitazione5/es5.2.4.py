R_0 = 220
V_S = 40
R_S = 8

max_P = 0
max_n = 0.01

for n in range(1, 200):
    n /= 100
    p = R_S * (((n * V_S) / (((n ** 2) * R_0) + R_S))) ** 2

    (max_P, max_n) = (p, n) if p > max_P else (max_P, max_n)

    print(f"n = {n}\tP = {p}")

print(f"Rapporto avvolgimenti:\t{max_n}\nPotenza:\t{max_P}")
