def convert_points_in_numbers(l):
    return [int(e) for e in l]


def get_data_from_file(path):
    l = []
    with open(path) as in_file:
        for line in in_file:
            line = line.rstrip().split(";")
            l.append(
                {
                    "name": f"{line[0]}-{line[1]}",
                    "points": convert_points_in_numbers(line[2:]),
                }
            )
    return l


def order_by_points(l):
    return sorted(l, key=lambda x: sum(x["points"]), reverse=True)


def print_ranking(l):
    for e in l:
        name = e["name"].split("-")
        print(f"{name[0]:15}{name[1]:20}{sum(e["points"])}")


def most_of(l, p):
    return max(l, key=lambda x: x["points"].count(p))


def main():
    FILE_NAME = "bowling.txt"
    
    points = get_data_from_file(FILE_NAME)

    print(f"\n{"Classifica":>25}\n\n")

    print_ranking(order_by_points(points))

    person_most_strike = most_of(points, 10)
    
    if person_most_strike["points"].count(10) > 0:
        print(
            f"\n{" ".join(person_most_strike["name"].split("-"))} ha fatto strike {person_most_strike["points"].count(10)} volta/e"
        )
    else:
        print("\nNessuno dei partecipanti ha fatto strike")

    person_most_miss = most_of(points, 0)
    
    if person_most_miss["points"].count(0) > 0:   
        print(
            f"{" ".join(person_most_miss["name"].split("-"))} ha mancato tutti i birilli {person_most_miss["points"].count(0)} volta/e"
        )
    else:
        print("Tutti i partecipanti hanno sempre colpito almeno 1 birillo")


main()
