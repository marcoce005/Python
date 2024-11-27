def print_mat(m):
    for r in m:
        print(*r)


def fill_with_one(m):
    for r in m:
        for i in range(len(r)):
            r[i] = 1


def fill_mat_chessboard(m):
    swap = True

    for r in m:
        for i in range(len(r)):
            r[i] = (i + int(swap)) % 2
        swap = not swap


def change_coloums(m):
    for r in m:
        r[0] = 1
        r[-1] = 1


def sum_mat(m):
    tot = 0
    [[tot := tot + e for e in r] for r in m]
    return tot


M = 10
N = 11

mat = [[0 for _ in range(N)] for e in range(M)]

print_mat(mat)
print()

fill_with_one(mat)
print_mat(mat)
print()

fill_mat_chessboard(mat)
print_mat(mat)
print()

mat[0] = [0] * N
mat[-1] = [0] * N

print_mat(mat)
print()

change_coloums(mat)
print_mat(mat)
print()

print(f"Somma valori:\t{sum_mat(mat)}")
