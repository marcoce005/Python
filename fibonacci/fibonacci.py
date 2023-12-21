def fibonacci(a, b):
    tot = a + b
    print(tot, "\n")
    return tot

n1 = float(0)
n2 = float(1)
print(n2, "\n")
while True:
    c = fibonacci(n1, n2)
    if n1 > n2:
        n2 = c
    else:
        n1 = c