from pprint import pprint


def get_moves(path):
    l = []
    with open(path) as in_file:
        for line in in_file:
            line = line.rstrip().split()
            l.append((line[0], int(line[1])))
    return l


def print_grid(g):
    for r in range(len(g[0]) - 1, -1, -1):
        for c in range(len(g)):
            print(f"{"-" if g[c][r] == "0" else g[c][r]}", end="")
        print()


def put_disk(g, col, type):
    g[col][g[col].index("0")] = type


def check_horizontal(g, r, c, v):
    try:
        return g[r][c] + g[r][c + 1] + g[r][c + 2] + g[r][c + 3] == v * 4
    except:
        return False


def check_vertical(g, r, c, v):
    try:
        return g[r][c] + g[r + 1][c] + g[r + 2][c] + g[r + 3][c] == v * 4
    except:
        return False


def check_diagonal(g, r, c, v):
    try:
        return g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2] + g[r + 3][c + 3] == v * 4
    except:
        return False


def check_win(g, type):
    for r in range(len(g)):
        for c in range(len(g[0])):
            if (
                check_horizontal(g, r, c, type)
                or check_vertical(g, r, c, type)
                or check_diagonal(g, r, c, type)
            ):
                return True

    return False


def play_game(gr, mv):
    for i, e in enumerate(mv):
        print(f"\nGioca il giocatore {e[0]}")
        put_disk(gr, e[1], "O" if e[0] == "G1" else "X")
        print_grid(gr)

        if check_win(gr, "O" if e[0] == "G1" else "X"):
            print(f"\nHa vinto {e[0]} in {i + 1} mosse")
            return


def main():
    PATH_MOVES = "./mosse.txt"

    grid = [["0" for _ in range(6)] for _ in range(7)]
    moves = get_moves(PATH_MOVES)

    print("Griglia vuota")
    print_grid(grid)

    play_game(grid, moves)


main()
