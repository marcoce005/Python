from pprint import pprint
from random import choice


def get_infos_by_file(path):
    maze = []
    with open(path) as in_file:
        start = tuple([int(e) for e in in_file.readline().rstrip().split(",")])
        finish = tuple([int(e) for e in in_file.readline().rstrip().split(",")])

        for line in in_file:
            maze.append(list(line.rstrip()))
    return start, finish, maze


def where_he_can_go(c, m):
    possible_place = []
    for e in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if m[c[0] + e[0]][c[1] + e[1]] not in "XV":
            possible_place.append((c[0] + e[0], c[1] + e[1]))
    return possible_place


def find_exit_of_maze(s, f, m):
    coord = s
    elenco_movimenti = []
    count = 1

    print(f"posizione iniziale: ({coord[0]}, {coord[1]})")
    while coord != f:
        m[coord[0]][coord[1]] = "V"
        possible_direction = where_he_can_go(coord, m)

        if len(possible_direction) > 0:
            elenco_movimenti.append(coord)
            coord = choice(possible_direction)
        else:
            coord = elenco_movimenti.pop(-1)

        print(f"movimento {count}: ({coord[0]}, {coord[1]})")

        count += 1


def main():
    FILE_PATH = "./labirinto.txt"

    start, finish, maze = get_infos_by_file(FILE_PATH)

    find_exit_of_maze(start, finish, maze)


main()
