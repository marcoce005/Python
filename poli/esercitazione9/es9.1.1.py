def swap_first_last(l):
    l[0], l[-1] = l[-1], l[0]


def shift_right(l):
    l.insert(0, l.pop(-1))


def replace_even(l, v):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = v


def replace_with_major(l):
    for i in range(1, len(l) - 1):
        l[i] = l[i + 1] if l[i + 1] > l[i - 1] else l[i - 1]


def del_central(l):
    (l.pop(len(l) // 2), l.pop(len(l) // 2)) if len(l) % 2 == 0 else l.pop(len(l) // 2)


def move_even(l):
    return [(e, l.remove(e))[0] for e in l if e % 2 == 0] + l


def find_second_max(l):
    tmp = [*l]
    return max([e for e in tmp if e != max(tmp)])


l = [e for e in range(10)]

print(f"Before:\t{l}")
swap_first_last(l)
print(f"After:\t{l}")

print(f"\nBefore:\t{l}")
shift_right(l)
print(f"After:\t{l}")

print(f"\nBefore:\t{l}")
replace_even(l, 0)
print(f"After:\t{l}")

print(f"\nBefore:\t{l}")
replace_with_major(l)
print(f"After:\t{l}")

print(f"\nBefore:\t{l}")
del_central(l)
print(f"After:\t{l}")

print(f"\nBefore:\t{l}")
print(f"Massimo II:\t{find_second_max(l)}")
