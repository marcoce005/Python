n = int(input("Inserire un numero intero:\t"))

for i in range(n):
    prime = True if i > 1 else False
    [prime := False for j in range(2, i) if i % j == 0]
    print(i) if prime else None
