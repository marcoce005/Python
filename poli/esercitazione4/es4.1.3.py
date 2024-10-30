n = int(input("Inserire un numero intero:\t"))

print((("*" * n) + "\n") * n, "\n\n")

s = 1
[(print(" " * (n - 1 - i) + "*" * s), s := s + 2) for i in range(n)]
s -= 2
[(s := s - 2, print(" " * (i + 1) + "*" * s)) for i in range(n)]
