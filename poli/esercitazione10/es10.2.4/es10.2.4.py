def get_data():
    with open("./bond_data.txt", "r") as bond:
        return [line.rstrip().rsplit(" ", 2) for line in bond]


def filter_data(data, value):
    return [l for l in data if value in l]


def formatted_print(l):
    print(f"{"Bond":>20}{"Bond Energy":>30}{"Bond Length":>20}")
    for e in l:
        print(f"{e[0]:>20}{e[1]:>20} kJ/mol{e[2]:>20} nm")


bond_data = get_data()

search = input("Inserire il dato da cercare:\t")

formatted_print(filter_data(bond_data, search))
