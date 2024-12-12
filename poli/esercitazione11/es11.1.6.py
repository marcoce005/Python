def eratostene_primes(s, i, n):
    if i > n**0.5:
        return s
    return eratostene_primes({e for e in s if e == i or e % i != 0}, i + 1, n)


n = input("Inserire un numero, che sarà il limite dei numeri primi [default = 10]:\t")

n = 10 if n == "" else int(n)

initial_set = {i for i in range(2, n + 1)}

print(eratostene_primes(initial_set, 2, n))
