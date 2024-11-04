n = input("Inserire un numero intero:\t")
n_even = n_odd = tot = 0
min = max = int(n) if n != "" else None

while n != "":
    n = int(n)
    tot += n
    min = n if n < min else min
    max = n if n > max else max

    if n % 2 == 0: 
        n_even += 1
    else: 
        n_odd += 1

    print(f"Somma parziale:\t{tot}\nMin:\t{min}\nMax:\t{max}\nPari:\t{n_even}\nDispari:\t{n_odd}")
    n = input("Inserire un numero intero:\t")
