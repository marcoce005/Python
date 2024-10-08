import pandas as pd  # sudo pacman -S python-pandas
import matplotlib.pyplot as plt  # sudo pacman -S python-matplotlib
from sys import argv


def sum_hours(h1, h2):
    hh = int(h1.split(":")[0]) + int(h2.split(":")[0])
    mm = int(h1.split(":")[1]) + int(h2.split(":")[1])
    mm, hh = mm % 60, hh + (mm // 60) if mm > 59 else hh
    return str(hh).zfill(2) + ":" + str(mm).zfill(2)


def get_data_from_file():
    try:
        with open("/home/marco/uptime_report/uptime.txt") as file:
            lines = file.read()[:-1].split("\n")
            day_hour = {}
            [
                (
                    day_hour.update({e[0]: e[1]})
                    if e[0] not in day_hour
                    else day_hour.update({e[0]: sum_hours(e[1], day_hour[e[0]])})
                )
                for e in [el.split(" --> ") for el in lines]
            ]
            return day_hour

    except FileExistsError:
        print("\nIl file non esiste!")


def convert_hours_for_graph(list_hours):
    return [
        round(int(e[0]) + int(e[1]) / 60, 2)
        for e in [el.split(":") for el in list_hours]
    ]


def decimal_2_hours(time):
    time = str(time).split(".")
    return time[0].zfill(2) + ":" + str(round(float(time[1]) * 0.6)).zfill(2)


try:
    visible_days = int(argv[1])
except:
    print("Wrong argument, only integer number")
    exit()

if visible_days <= 0:
    print("Argument must be greater than 0, if you want see something")
    exit()

uptime_infos = dict(list(get_data_from_file().items())[-(visible_days):])

print(uptime_infos)

dati_utilizzo = {
    "Giorno": list(uptime_infos.keys()),
    "Ore": convert_hours_for_graph(list(uptime_infos.values())),
}

# Crea un DataFrame
df = pd.DataFrame(dati_utilizzo)

# Imposta il giorno come indice
df.set_index("Giorno", inplace=True)

# Crea il grafico
plt.figure(figsize=(10, 6))

plt.bar(df.index, df["Ore"], color="skyblue")
for index, value in enumerate(df["Ore"]):
    plt.text(index, value + 0.1, str(decimal_2_hours(value)), ha="center")

plt.xlabel("Giorno della settimana")
plt.ylabel("Ore di utilizzo")
plt.title("Utilizzo del computer per giorno della settimana")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Mostra il grafico
plt.tight_layout()
plt.show()
