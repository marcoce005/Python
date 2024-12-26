def print_mat(m):
    for r in m:
        print(*r)


def print_mat_with_dot(m):
    for r in m:
        for e in r:
            print("." if not e[1] else e[0], end="")
        print()


def get_data(path):
    with open(path) as in_file:
        return [[[e, False] for e in line.rstrip()] for line in in_file]


def check_horizontal(x, y, m, w):
    l = [c for c, s in m[x][y : y + 4]]
    if l == list(w) or l == list(w[::-1]):
        for i in range(4):
            m[x][y + i][1] = True
        return 2 if l == list(w) and l == list(w[::-1]) else 1
    return 0


def check_vertical(x, y, m, w):
    l = [m[x + i][y][0] for i in range(4)]
    if l == list(w) or l == list(w[::-1]):
        for i in range(4):
            m[x + i][y][1] = True
        return 2 if l == list(w) and l == list(w[::-1]) else 1
    return 0


def check_negative_diagonal(x, y, m, w):
    l = [m[x + i][y + i][0] for i in range(4)]
    if l == list(w) or l == list(w[::-1]):
        for i in range(4):
            m[x + i][y + i][1] = True
        return 2 if l == list(w) and l == list(w[::-1]) else 1
    return 0


def check_positive_diagonal(x, y, m, w):
    l = [m[x + i][y - i][0] for i in range(4)]
    if l == list(w) or l == list(w[::-1]):
        for i in range(4):
            m[x + i][y - i][1] = True
        return 2 if l == list(w) and l == list(w[::-1]) else 1
    return 0


def find_XMAS(m, w):
    tot = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            tot += (
                check_horizontal(i, j, m, w)
                + (check_vertical(i, j, m, w) if i <= len(m) - len(w) else 0)
                + (
                    check_negative_diagonal(i, j, m, w)
                    if i <= len(m) - len(w) and j <= len(m[i]) - len(w)
                    else 0
                )
                + (
                    check_positive_diagonal(i, j, m, w)
                    if j >= len(w) - 1 and i <= len(m) - len(w)
                    else 0
                )
            )
    return tot


def main():
    FILE_NAME = "./test.txt"
    WORD = "XMAS"

    matrix_letters = get_data(FILE_NAME)

    XMAS_found = find_XMAS(matrix_letters, WORD)

    # print_mat(matrix_letters)
    print_mat_with_dot(matrix_letters)
    print(f"\n\nWe found {XMAS_found} XMAS")


main()
