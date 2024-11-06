from random import randint

"""

0 --> dritto
1 --> destra
2 --> indietro
3 --> sinistra

"""

x = 0
y = 0

for i in range(100):
    n = randint(0, 4)
    if n % 2 == 0:
        y += 1 if n == 0 else -1
    else:
        x += 1 if n == 1 else -1

print(f"Il bro arriva a ({x}, {y})\nSi è spostato di {((x ** 2) + (y ** 2)) ** 0.5:.2f} dall'origine")
