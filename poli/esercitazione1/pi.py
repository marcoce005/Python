def is_prime(n):
    acc = False
    for i in range(2, n):
        if n % i == 0: return False
    return True


def next_prime(n):
    while not is_prime(n + 1):
        n += 1
    return n + 1

decimal_digit = 4
pi = 1 - 1/3
sign = True
prime = 3
n = 0

while n < 1000:
    prime = next_prime(prime)
    pi += 1 / prime if sign else -1 / prime
    sign = not sign
    n += 1

print(pi * 4)
