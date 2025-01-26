def get_schedine(path):
    l = []
    with open(path) as in_file:
        for line in in_file:
            line = line.rstrip().split(",")
            l.append(
                {
                    "id_schedina": int(line[0]),
                    "numeri": line[1:7],
                    "costo": float(line[-1]),
                }
            )
    return l


def get_vincete(path):
    with open(path) as in_file:
        return in_file.readline().rstrip().split()


def get_premi(path):
    with open(path) as in_file:
        return list(reversed([int(line.rstrip().split()[1]) for line in in_file]))


def cal_vendite(s):
    return sum([e["costo"] for e in s])


def check_winner(s, v, p):
    premi_dati = 0
    winners = []

    print("Schedine Vincenti:")
    for e in s:
        correct_number = []
        for n in e["numeri"]:
            correct_number.append(n) if n in v or n == "*" else None

        if len(correct_number) > 2:
            winners.append(
                {
                    "id_schedina": e["id_schedina"],
                    "numeri": correct_number,
                    "vincita": p[len(correct_number) - 1],
                    "tipo_premio": len(correct_number),
                }
            )
            premi_dati += p[len(correct_number) - 1]

    return sorted(winners, key=lambda x: x["vincita"], reverse=True), premi_dati


def print_output(w, cost, sells):
    if w == 0:
        print(
            f"Nessuna schednina ha vinto\nGuadagno netto degli organizzatori: {sells} euro"
        )
        return

    print("Schedine Vincenti:")
    for e in w:
        print(
            f"ID_SCHEDINA: {e["id_schedina"]} NUMERI_INDOVINATI:",
            *e["numeri"],
            sep=" ",
            end=" ",
        )
        print(f"VINCITA: {e["vincita"]} TIPO PREMIO: {e["tipo_premio"]}")

    print(f"\nGuadagno netto degli organizzatori: {sells - cost} euro")


def main():
    PATH_SCHEDINE = "./schedine.txt"
    PATH_VINCENTE = "./vincente.txt"
    PATH_PREMI = "./premi.txt"

    schedine = get_schedine(PATH_SCHEDINE)
    vincente = get_vincete(PATH_VINCENTE)
    premi = get_premi(PATH_PREMI)
    vendite = cal_vendite(schedine)
    winners, costo = check_winner(schedine, vincente, premi)

    print_output(winners, costo, vendite)


main()
