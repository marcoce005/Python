def print_maze(m, p):
    for r in range(len(m)):
        for c in range(len(m[r])):
            print(p[(r, c)] if m[r][c] != "*" else "*", end="")
        print()


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
    return {
        (r, c): get_neighbours(m, r, c)
        for r in range(len(m))
        for c in range(len(m[r]))
        if m[r][c] == " "  # and len(get_neighbours(m, r, c)) > 0
    }


def create_dictionary_paths(cor):
    return {k: "?" for k in cor.keys()}


def print_dict(d):
    print(f"Coordinates --> Neighbours\n")
    for k, v in d.items():
        print(f"{k} --> {v}")


def fill_borders(p, m):
    for k in p.keys():
        if k[0] == 0:
            p[k] = "N"
        elif k[0] == len(m) - 1:
            p[k] = "S"
        elif k[1] == 0:
            p[k] = "W"
        elif k[1] == len(m[k[0]]) - 1:
            p[k] = "E"


def find_where_is(a, b):
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]

    if delta_x < 0:
        return "S"
    elif delta_x > 0:
        return "N"
    elif delta_y < 0:
        return "E"
    elif delta_y > 0:
        return "W"


def fill_others(c, p):
    edit_something = False
    for k, v in c.items():
        if p[k] == "?":
            for e in v:
                if p[e] != "?":
                    p[k] = find_where_is(k, e)
                    edit_something = True

    return fill_others(c, p) if edit_something else None


maze = get_maze()

corridors = create_dictionary_corridos(maze)

paths = create_dictionary_paths(corridors)

fill_borders(paths, maze)

fill_others(corridors, paths)

print_maze(maze, paths)
