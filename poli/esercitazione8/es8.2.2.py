def fill_matrix(m):
    for r in m:
        for i in range(len(r)):
            r[i] = int(input("Insererire i numeri:\t"))


def print_mat(m):
    for r in m:
        for e in r:
            print(f"{e:4d}", end="")
        print()


def flat(m):
    l = []
    [l := l + r for r in m]
    return l


def check_num(m):
    return flat(m) == [i + 1 for i in range(16)]


def get_colums(m):
    return [[m[j][i] for j in range(4)] for i in range(4)]


def get_cross(m):
    return [m[i][i] for i in range(4)], [m[i][3 - i] for i in range(4)]


def is_perfect(m):
    l = [*m, *get_colums(m), *get_cross(m)]
    base = sum(m[0])

    for e in l:
        if sum(e) != base:
            return False
    return True


m = [[0] * 4 for _ in range(4)]

fill_matrix(m)

print_mat(m)

print(f"Contine solo numeri da 1 a 16:\t{check_num(m)}")

print(f"Is perfect:\t{is_perfect(m)}")
