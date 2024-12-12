from csv import reader


def get_states_incomes_txt():
    with open("./rawdata_2004.txt", "r") as data:
        return {
            line.split("$")[0]
            .split(maxsplit=1)[1]
            .rstrip(): int(line.split("$")[1].strip().replace(",", ""))
            for line in data
        }


def get_states_incomes_csv():
    with open("./rawdata_2021.csv", "r") as data:
        data.readline()
        return {line[0]: int(line[2][1:].replace(",", "")) for line in reader(data)}


# states_incomes = get_states_incomes_txt()

states_incomes = get_states_incomes_csv()

user_input = input(
    "\nInserire il nome del paese da ricercare [quit per uscire]:\t"
).title()
while user_input.lower() != "quit":
    if user_input in states_incomes.keys():
        print(f"\n{user_input} --> {states_incomes[user_input]} $")
    else:
        print("\nPaese non presente nel dataset")

    user_input = input(
        "\nInserire il nome del paese da ricercare [quit per uscire]:\t"
    ).title()
