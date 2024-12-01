from pprint import pprint


def check_seat(x, y, r, c):
    return x >= 0 and x < r and y >= 0 and y < c


def find_seat_by_prize(m, prize):
    for x, r in enumerate(m):
        if prize in r:
            y = r.index(prize)
            return x, y


seats = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30],
]

print("Posti in sala e relativo prezzo [dove c'è 0 è occupato]\n\n")
pprint(seats)

n = input(
    "\n\nMetodi di selezione del posto:\n\tcoordinate [es. 1,2 oppure 4,0]\n\tcosto del biglietto [es. 20 oppure 40]\n\tterminare [es. exit]\n-->"
)

while n.lower() != "exit":
    if "," in n:
        x, y = int(n.split(",")[0]), int(n.split(",")[1])

        if check_seat(x, y, len(seats), len(seats[0])):
            if seats[x][y] == 0:
                print("\nPosto occupato sceglierne un altro.")
            else:
                print(
                    f"Perfetto ti è stato assegnato il posto ({x},{y})\nSono {seats[x][y]}€"
                )
                seats[x][y] = 0
        else:
            print("Posto inesistente")
    elif n.isdigit():
        x, y = find_seat_by_prize(seats, int(n))
        print(f"Perfetto ti è stato assegnato il posto ({x},{y})\nSono {seats[x][y]}€")
        seats[x][y] = 0
    elif n != "exit":
        print("Input invalido, riprovare!")

    print("Posti in sala e relativo prezzo [dove c'è 0 è occupato]\n\n")
    pprint(seats)
    n = input(
        "\n\nMetodi di selezione del posto:\n\tcoordinate [es. 1,2 oppure 4,0]\n\tcosto del biglietto [es. 20 oppure 40]\n\tterminare [es. exit]\n-->"
    )
