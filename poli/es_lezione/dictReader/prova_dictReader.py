from csv import DictReader


def get_data_from_file(path):
    with open(path) as file:
        reader = DictReader(
            file, fieldnames=["number", "CF"]
        )  # in fieldnames passi la struttura che vuoi dare al tuo dizionario

        print(*reader, sep="\n")


dict_num_tel = get_data_from_file("./num_tel.csv")
