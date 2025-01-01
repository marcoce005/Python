from csv import DictReader


# use the method DictReader to get all the infos from file
# and create a list of dictionary in base of the file's info
def get_flights_from_file(path):
    with open(path) as in_file:
        return list(
            DictReader(
                in_file,
                ["flight_id", "city_destination", "number_passengers"],
                delimiter=";",
            )
        )


def get_weather_from_file(path):
    with open(path) as in_file:
        return list(
            DictReader(
                in_file,
                ["city", "weather_condition"],
                delimiter=";",
            )
        )


# calculate the average of passengers
# filter unnecessary information from flights and sum only numerber of passengers using the function sum()
def avg_passengers(l):
    return sum([int(e["number_passengers"]) for e in l]) / len(l)


def print_rainy_stormy(f, w):
    print("\nCodice dei voli verso città con condizione meteorologica Rainy o Stormy:")

    # create a dictionary where keys are the cities and the value are the weather condition
    w = {e["city"]: e["weather_condition"] for e in w}

    # select only the flight that have a "Rainy" or "Stormy" city of destination
    for e in f:
        if e["city_destination"] in w and w[e["city_destination"]] in [
            "Rainy",
            "Stormy",
        ]:
            print(
                f" * {e["flight_id"]} verso {e["city_destination"]}: {w[e["city_destination"]]}"
            )


# filter flights by city name and create a list of only the number of passangers for that city and sum all together
def get_all_passengers_from_that_city(f, city):
    return sum(
        [int(e["number_passengers"]) for e in f if e["city_destination"] == city]
    )


def print_cities(f, w):
    # create a set of possible cities (to eliminate the duplicate)
    cities = set([e["city_destination"] for e in f])
    # create a dictionary where keys are the cities and the value are the weather condition
    weathers = {e["city"]: e["weather_condition"] for e in w}

    print(
        "\nCondizione meteorologica delle città che sono destinazione di almeno un volo:"
    )
    for city in cities:
        print(
            f"{city}: {weathers[city]}. {get_all_passengers_from_that_city(f, city)} passeggeri in arrivo."
        )


def main():
    # files paths
    FLIGHTS_PATH = "./flights.txt"
    WEATHER_PATH = "./weather.txt"

    # check if the files exists
    try:
        flights = get_flights_from_file(FLIGHTS_PATH)
        weather = get_weather_from_file(WEATHER_PATH)
    except FileNotFoundError as err:
        print("File non trovato:\n", err)
        return

    print(f"Numero medio di passegeri: {avg_passengers(flights)}")

    print_rainy_stormy(flights, weather)

    print_cities(flights, weather)


main()
