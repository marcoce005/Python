import csv


def get_stat(path):
    with open(path) as file:
        return list(csv.DictReader(file, delimiter=";"))


def get_regions(path):
    with open(path) as file:
        return [line.rstrip() for line in file]


def filter_by_region(stat, regions):
    return [e for e in stat if e["Denominazione Regione"] in regions]


def count_cities(l, region):
    return len(filter_by_region(l, [region]))


def sort_alphabetic_cities(l):
    return sorted(l, key=lambda x: x["Denominazione in italiano"])


def find_smallest_biggest_name(l, min_or_max):
    return (
        min(
            sort_alphabetic_cities(l), key=lambda x: len(x["Denominazione in italiano"])
        )["Denominazione in italiano"]
        if min_or_max
        else max(
            sort_alphabetic_cities(l), key=lambda x: len(x["Denominazione in italiano"])
        )["Denominazione in italiano"]
    )


def main():
    FILE_STAT = "./elenco-comuni-italiani.csv"
    FILE_REGION = "./regioni.txt"

    try:
        regions = get_regions(FILE_REGION)
        stat_regions = filter_by_region(get_stat(FILE_STAT), regions)

        for r in regions:
            print(f"*** REGIONE {r} ***")
            print(f"Nella regione Lazio ci sono {count_cities(stat_regions, r)} comuni")
            print(
                f"Il nome più breve è {find_smallest_biggest_name(filter_by_region(stat_regions, [r]), True)} e quello più lungo è {find_smallest_biggest_name(filter_by_region(stat_regions, [r]), False)}"
            )
    except FileNotFoundError:
        print("Path dei/del file errato\n")
    except Exception as err:
        print(
            "C'è stato un problema nell'esecuzione del programma\nControllare la correttenza dei file\n",
            err,
        )


main()
