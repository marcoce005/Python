def get_menu_from_file(path):
    d = {}
    with open(path) as file:
        for line in file:
            line = line.rstrip().split(", ")
            d[line[0]] = {
                "name": line[1],
                "prize": float(line[2]),
                "IVA": float(line[3]),
            }
    return d


def get_ordine_from_file(path):
    d = {}
    with open(path) as file:
        for line in file:
            line = line.rstrip().split(", ")
            d[line[0]] = int(line[1])
    return d


def add_IVA_to_ordine_sort_by_IVA(ordine, menu):
    for e in ordine:
        ordine[e] = [ordine[e], menu[e]["IVA"]]

    return dict(sorted(ordine.items(), key=lambda x: x[1][1]))


def print_scontrino(ordine, menu):
    tot = 0
    IVA = 0
    print("RICEVUTA")
    for k, v in ordine.items():
        tot += menu[k]["prize"] * v[0]
        IVA += (menu[k]["prize"] - (menu[k]["prize"] / (1 + v[1] / 100))) * v[0]
        print(
            f" {v[0]}  {menu[k]["name"]:30} {menu[k]["prize"] * v[0]:10.2f} IVA {v[1]:5.2f}%"
        )

    print(f"\nTotale: {tot:.2f}€\nDi cui IVA: {IVA:.2f}€")


def main():
    MENU_PATH = "./menu.txt"
    ORDINE_PATH = "./ordine.txt"

    try:
        menu = get_menu_from_file(MENU_PATH)
        ordine = get_ordine_from_file(ORDINE_PATH)
    except FileNotFoundError as err:
        print("File non trovato:\n", err)
        return

    ordine_sorted = add_IVA_to_ordine_sort_by_IVA(ordine, menu)

    print_scontrino(ordine_sorted, menu)


main()
