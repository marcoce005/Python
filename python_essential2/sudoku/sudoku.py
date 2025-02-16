def get_sudoku_matrix(path):
    with open(path) as file:
        return [list(line.rstrip()) for line in file]


def check_is_correct(m):
    numbers = set(str(i + 1) for i in range(9))
    neighbours = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]
    permutation = [
        (e, f) for e in [0, 3, 6] for f in [0, 3, 6]
    ]  # permutation of [0, 3, 6] that rapresent the index of each square 3x3

    for i in range(9):
        if set(m[i]) != numbers or set([m[j][i] for j in range(9)]) != numbers:
            return False

        r, c = permutation[i]
        if set([m[r + e[0]][c + e[1]] for e in neighbours]) != numbers:
            return False
    return True


FILE_PATH = "test1.txt"

mat = get_sudoku_matrix(FILE_PATH)

print(f"\nThe soduku is correct?:\t{'Yes' if check_is_correct(mat) else 'No'}")
