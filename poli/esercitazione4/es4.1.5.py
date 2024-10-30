n = int(input("Inserire un numero intero:\t"))

prime = True
[prime := False for i in range(2, n) if n % i == 0]

print(f"Il numero {n} {'è primo' if prime else 'non è primo'}")
