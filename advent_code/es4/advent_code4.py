def print_mat(m):
    for r in m:
        print(*r)


def get_data(path):
    with open(path) as in_file:
        return [[[e, False] for e in line.rstrip()] for line in in_file]


def check_right(x, y, m, w):
    if [c for c, s in m[x][y : y + 4]] == list(w):
        for i in range(4):
            m[x][y + i][1] = True


def check_left(x, y, m, w):
    if [c for c, s in m[x][y - 3 : y + 1]] == list(w[::-1]):
        for i in range(4):
            m[x][y - i][1] = True


def check_down(x, y, m, w):
    if [m[x + i][y][0] for i in range(4)] == list(w):
        for i in range(4):
            m[x + i][y][1] = True


def check_up(x, y, m, w):
    if [m[x - i][y][0] for i in range(4)] == list(w):
        for i in range(4):
            m[x - i][y][1] = True


def find_XMAS(m, w):
    for i in range(len(m)):
        for j in range(len(m[i])):
            check_right(i, j, m, w)
            check_left(i, j, m, w) if j >= len(w) - 1 else None
            check_down(i, j, m, w) if i <= len(m) - 1 - len(w) else None
            check_up(i, j, m, w) if i >= len(w) - 1 else None


def main():
    FILE_NAME = "./input.txt"
    WORD = "XMAS"

    matrix_letters = get_data(FILE_NAME)

    find_XMAS(matrix_letters, WORD)

    print_mat(matrix_letters)


main()
