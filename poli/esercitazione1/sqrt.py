a = 3
n = 0
x_n = a / 2

while n < 1000:
    x_n = (x_n + a / x_n) / 2
    n += 1

print(x_n)
