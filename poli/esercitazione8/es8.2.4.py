import matplotlib.pyplot as plt
import numpy as np


def force(k, x):
    return -k * x


def acceleration(f, m):
    return f / m


K = 10

v = 0
m = 1
delta_t = 0.01
x = 0.5

list_v = [0]
list_a = [0]

while x > 0:
    a = acceleration(-force(K, x), m)
    delta_v = a * delta_t
    delta_s = v * delta_t + 0.5 * a * (delta_t**2)
    v += delta_v

    list_v.append(v)
    list_a.append(a)

    x -= delta_s

    print(f"Accellerazione:\t{a}\nVelocità:\t{v}\n")

time = [i * 0.01 for i in range(len(list_a))]

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(time, list_v, label="Velocità (m/s)", color="blue", linestyle="-", marker="o")
plt.plot(
    time,
    list_a,
    label="Accelerazione (m/s²)",
    color="red",
    linestyle="--",
    marker="x",
)

# Personalizzazione del grafico
plt.title("Andamento di Velocità e Accelerazione nel Tempo", fontsize=16)
plt.xlabel("Tempo (s)", fontsize=14)
plt.ylabel("Valori", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

# Mostrare il grafico
plt.show()
