def print_maze(m):
    for r in m:
        print(*r)


def get_maze():
    with open("./maze.txt") as file:
        return [list(line.replace("\n", "")) for line in file]


def exist_coordinates(m, x, y):
    return 0 <= x < len(m) and 0 <= y < len(m[x])


def get_neighbours(m, x, y):
    return [
        (x + e[0], y + e[1])
        for e in [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if exist_coordinates(m, x + e[0], y + e[1]) and m[x + e[0]][y + e[1]] != "*"
    ]


def create_dictionary_corridos(m):
    # cor = {}
    # for r in range(len(m)):
    #     for c in range(len(m[r])):
    #         if m[r][c] == " ":
    #             neighbours = get_neighbours(m, r, c)
    #             cor.update({(r, c): neighbours}) if len(neighbours) > 0 else None

    return {
        (r, c): get_neighbours(m, r, c)
        for r in range(len(m))
        for c in range(len(m[r]))
        if m[r][c] == " " and len(get_neighbours(m, r, c)) > 0
    }


def print_dict(d):
    print(f"Coordinates --> Neighbours\n")
    for k, v in d.items():
        print(f"{k} --> {v}")


maze = get_maze()

corridors = create_dictionary_corridos(maze)

print_dict(corridors)
