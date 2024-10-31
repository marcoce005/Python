from random import uniform, random, randint

def is_pow_2(n):
    while n != 1:
        if n % 2 != 0:
            return False
        n /= 2
    return True

n_marble = round(uniform(10, 100))
start = False# bool(round(random()))           # True --> start human, False --> start machine
computer_logic = False # bool(round(random()))      # True --> intelligent mode, False --> stupid mode

print(n_marble, start, computer_logic)

while n_marble - 1 != 0:
    if start:
        get_marble = int(input(f"Puoi prendere da 1 a {n_marble // 2} biglie [numero intero]:\t"))
        (print("Non puoi barare, rincomincia"), exit(1)) if get_marble < 1 or get_marble > n_marble // 2 else None
    else:
        if computer_logic:
            for i in range(n_marble // 2 if n_marble % 2 == 0 else (n_marble // 2) + 1, n_marble):
                if is_pow_2(i + 1):
                    print(i)
                    get_marble = n_marble - i
                    break
        else:
            get_marble = round(uniform(1, n_marble // 2))
        print(f"Il computer ha preso:\t{get_marble} biglie")
        exit(1)
    
