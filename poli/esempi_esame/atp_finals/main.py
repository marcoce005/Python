from random import random


def get_players_from_file(path):
    with open(path, "r") as in_file:
        return sorted(
            [
                (line.rstrip().split(",")[0], line.rstrip().split(",")[1])
                for line in in_file
            ],
            key=lambda x: x[0],
        )


def fill_groups(l, a, b):
    for i in range(0, len(l) - 1, 2):
        (
            (a.append(l[i]), b.append(l[i + 1]))
            if round(random())
            else (a.append(l[i + 1]), b.append(l[i]))
        )


def save_groups_in_file(a, b, file_a, file_b):
    with open(file_a, "w") as out_file:
        for e in a:
            out_file.write(f"{e[0]} - {e[1]}\n")

    with open(file_b, "w") as out_file:
        for e in b:
            out_file.write(f"{e[0]} - {e[1]}\n")


def create_calendar(a, b, caledar_file):
    output = "GIRONE VERDE\n"
    for i in range(len(a) - 1):
        output += f"Giornata {i + 1}:\n"

        choosen = set([a[0], a[i + 1]])
        others = list(set(a).difference(choosen))

        output += f"{a[0][1]} vs {a[i + 1][1]}\n"
        output += f"{others[0][1]} vs {others[1][1]}\n"

    output += "GIRONE ROSSO\n"
    for i in range(len(b) - 1):
        output += f"Giornata {i + 1}:\n"

        choosen = set([b[0], b[i + 1]])
        others = list(set(b).difference(choosen))

        output += f"{b[0][1]} vs {b[i + 1][1]}\n"
        output += f"{others[0][1]} vs {others[1][1]}\n"

    with open(caledar_file, "w") as out_file:
        out_file.write(output[:-1])


def main():
    FILE_PATH = "./qualificati.txt"
    FILE_GROUP_A = "./verde.txt"
    FILE_GROUP_B = "./rosso.txt"
    FILE_CALENDAR = "./calendar.txt"

    players = get_players_from_file(FILE_PATH)
    group_A = [players[0]]
    group_B = [players[1]]

    fill_groups(players[2:], group_A, group_B)

    save_groups_in_file(group_A, group_B, FILE_GROUP_A, FILE_GROUP_B)

    create_calendar(group_A, group_B, FILE_CALENDAR)


main()
