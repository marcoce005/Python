from random import randint


def remove_noise(l):
    for i, e in enumerate(l):
        if i == 0:
            l[i] = round((e + l[i + 1]) / 2, 5)
        elif i == len(l) - 1:
            l[i] = round((e + l[i - 1]) / 2, 5)
        else:
            l[i] = round((e + l[i + 1] + l[i - 1]) / 3, 5)


l = [randint(15, 20) for _ in range(10)]

print("Lista:\t", *l)

remove_noise(l)

print("Lista senza rumore:\t", *l)
