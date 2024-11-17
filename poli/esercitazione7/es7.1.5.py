def same_set(a, b):
    for e in a:
        if e not in b:
            return False

    for e in b:
        if e not in a:
            return False

    return True


l1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
l2 = [11, 11, 7, 9, 16, 4, 1]


print(f"{l1} == {l2} ???\n{same_set(l1, l2)}")
