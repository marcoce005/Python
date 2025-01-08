def get_over_range_from_file(path):
    SOGLIA = 200
    d = {}
    with open(path, "r") as in_file:
        for line in in_file:
            if int(line.rstrip().split()[2]) >= SOGLIA:
                line = line.rstrip().split()

                if line[0] in d:
                    d[line[0]].append((line[1], line[2]))
                else:
                    d[line[0]] = [(line[1], line[2])]
    return d


def sort_by_over_range(d):
    return dict(sorted(d.items(), key=lambda x: len(x[1]), reverse=True))


def custom_print_dict(d):
    i = 0
    for k, v in d.items():
        for e in v:
            print(k, e[0], e[1])
        print() if i < len(d.items()) - 1 else None
        i += 1


def main():
    FILE_PATH = "./glucometers.txt"

    try:
        over_range = get_over_range_from_file(FILE_PATH)
    except FileNotFoundError as err:
        print("File non trovato\n", err)
        return
    except Exception as err:
        print("Qualcosa è andato storto:\n", err)

    sorted_over_range = sort_by_over_range(over_range)

    custom_print_dict(sorted_over_range)


main()
