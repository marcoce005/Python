def is_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True

def next_prime(n):
    """
    while not is_prime(n + 1):
        n += 1
    return n + 1
    """

    return n + 1 if is_prime(n + 1) else next_prime(n + 1)


n = int(input("Inserire un numero [intero]:\t"))
prime = 2

print(f"{n} = ")

while n != 1:
    if n % prime == 0:
        n /= prime
        print(prime)
    else:
        prime = next_prime(prime)
