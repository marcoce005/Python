from random import random, randint
from math import log2

def is_pow_2(n):
    return log2(n) % 1 == 0

n_marble = randint(10, 100)
start = bool(round(random()))           # True --> start human, False --> start machine
computer_logic = bool(round(random()))      # True --> intelligent mode, False --> stupid mode

print(f"Biglie = {n_marble}\n\nInizia:\t{'Tu' if start else 'Computer'}\n\nLogica computer:\t{'intelligent mode' if computer_logic else 'stupid mode'}\n")

while n_marble - 1 != 0:
    print(f"Biglie rimaste = {n_marble}")
    if start:
        get_marble = int(input(f"Puoi prendere da 1 a {n_marble // 2} biglie [numero intero]:\t"))
        (print("Non puoi barare, rincomincia"), exit(1)) if get_marble < 1 or get_marble > n_marble // 2 else None
    else:
        if computer_logic:
            for i in range(n_marble // 2 if n_marble % 2 == 0 else (n_marble // 2) + 1, n_marble):
                if is_pow_2(i + 1):
                    get_marble = n_marble - i
                    break
        else:
            get_marble = randint(1, n_marble // 2)
        print(f"Il computer ha preso:\t{get_marble} biglie")

    n_marble -= get_marble
    start = not start

print("\n\n\t\tGAME OVER" if start else "\n\n\t\tHai Vinto!!!")
