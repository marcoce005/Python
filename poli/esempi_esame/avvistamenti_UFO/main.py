from csv import DictReader


def read_csv_ufo_sightings(path, file_format):
    with open(path, "r") as csv_file:
        return list(DictReader(csv_file, file_format, delimiter=","))


def most_sightings(l):
    county_sightings = {}
    for e in l:
        county_sightings[e["country"]] = (
            1
            if e["country"] not in county_sightings
            else county_sightings[e["country"]] + 1
        )
    return max(list(county_sightings.items()), key=lambda x: x[1])[0]


def find_the_longest_one(l):
    return dict(max(l, key=lambda x: float(x["duration"])))


def main():
    CSV_PATH = "./ufo_sightings.csv"
    FILE_FORMAT = ["date", "time", "country", "shape", "duration", "description"]

    try:
        ufo_sightings = read_csv_ufo_sightings(CSV_PATH, FILE_FORMAT)

        country_with_most_signtings = most_sightings(ufo_sightings)
        print(
            "Paese con il maggior numero di avvistamenti: ", country_with_most_signtings
        )

        logest_sighting = find_the_longest_one(ufo_sightings)
        print(
            f"Avvistamento di durata più lunga: {logest_sighting["description"]} (Durata: {logest_sighting["duration"]} secondi, Forma: {logest_sighting["shape"]})"
        )

    except FileNotFoundError as err:
        print("\nPath del file non corretto.\n", err)
    except Exception as err:
        print("\nQualcosa è andato storto durante l'esecuzione del programma.\n", err)


main()
