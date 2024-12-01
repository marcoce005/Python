def filter_min_max(l):
    minimun = min(l)
    maximun = max(l)
    return [e for e in l if e != minimun and e != maximun]


def filter_even(l):
    return [e for e in l if e % 2 == 0]


def filter_2_digit(l):
    return [e for e in l if len(str(e)) == 2]


n = input(
    "Inserire la seguenza di numeri interi seguento il seguente formato [1:2:3:4]:\t"
).split(":")

n = [int(e) for e in n]

print("\nSenza il min e max:\t", end="")
print(*filter_min_max(n), sep=":")

print("\nSolo pari:\t", end="")
print(*filter_even(n), sep=":")

print("\nSolo con 2 cifre:\t", end="")
print(*filter_2_digit(n), sep=":")
