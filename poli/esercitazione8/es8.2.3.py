def print_mat(m):
    print("----" * 3)
    for r in m:
        for e in r:
            print(f"¦ {e} ", end="")
        print("¦\n" + "----" * 3)


def check_tie(m):
    for r in m:
        if " " in r:
            return False
    return True


def get_colums(m):
    return [[m[i][j] for i in range(3)] for j in range(3)]


def get_cross_neg(m):
    return [m[i][i] for i in range(3)]


def get_cross_pos(m):
    return [m[i][2 - i] for i in range(3)]


def check_win(m):
    l = (
        ["".join(r) for r in m]
        + ["".join(c) for c in get_colums(m)]
        + ["".join(get_cross_neg(m)), "".join(get_cross_pos(m))]
    )
    return "XXX" in l or "OOO" in l


m = [[" "] * 3 for _ in range(3)]
win = False
player = False

print_mat(m)

while not win:
    coord = input(
        f"Giocatore {"X" if player else "O"}\nInserire le coordinate [numeri tra 1 e 3] [es. x,y --> 1,2]:\t"
    ).split(",")
    x, y = int(coord[0]) - 1, int(coord[1]) - 1

    if m[x][y] == " ":
        m[x][y] = "X" if player else "O"
        player = not player
    else:
        print("Mossa non valida, riprova")

    print_mat(m)

    if check_win(m):
        print(f"\tVITTORIA GIOCATORE {"O" if player else "X"}")
        win = not win

    if check_tie(m) and not win:
        print("\t\tPARITA'")
        win = not win
