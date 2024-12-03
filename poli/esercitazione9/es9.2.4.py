def print_mat(m):
    for r in m:
        for e in r:
            print(f"{e:5d}", end="")
        print()


def find_end_spiral(l):
    return l // 2, (l // 2) - 1 if l % 2 == 0 else l // 2


def fill_spiral_matrix(m):
    r_centre, c_centre = find_end_spiral(len(m))
    i = 1
    plus = True
    column = True
    c = r = 0

    while m[r_centre][c_centre] == 0:
        m[r][c] = i
        i += 1

        if plus and column and (len(m) - 1 - r) == c:
            column = False
        elif plus and not column and r == c:
            plus = False
            column = True
        elif not plus and column and r + c == len(m) - 1:
            column = False
        elif (not plus) and (not column) and r - c == 1:
            column = plus = True

        n = 1 if plus else -1
        if column:
            c += n
        else:
            r += n


n = int(input("Inserire la dimensione della tabella [intero]:\t"))

m = [[0] * n for _ in range(n)]

fill_spiral_matrix(m)

print_mat(m)
