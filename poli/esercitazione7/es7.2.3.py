from random import randint


def filter_zero_stack(l):
    i = 0
    while i < len(l):
        i += (l.pop(i), 0)[1] if l[i] == 0 else 1


def sub_one(l):
    for i in range(len(l)):
        l[i] = l[i] - 1


def generate_stacks(c):
    l = []
    while c > 0:
        tmp = randint(1, c)
        l.append(tmp)
        c -= tmp
    return l


CARDS = 45

stacks = generate_stacks(CARDS)

filter_zero_stack(stacks)

print(stacks)

while stacks != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    add = len(stacks)
    sub_one(stacks)
    filter_zero_stack(stacks)
    stacks.append(add)

    print(stacks)


print(stacks)
