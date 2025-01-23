from csv import DictReader


def get_stat_from_csv(path):
    with open(path, "r") as csv_file:
        return list(DictReader(csv_file, delimiter=";"))


def get_queries_from_file(path):
    with open(path, "r") as in_file:
        return [tuple(line.rstrip().split()) for line in in_file]


def filter_by_country_values(country, values, co2):
    return {e["Anno"]: e[values] for e in co2 if e["Paese"] == country}


def country(para1, para2, co2):
    values_during_years = filter_by_country_values(para1, para2, co2)

    oldest_val = int(min(list(values_during_years.items()), key=lambda x: int(x[0]))[1])
    newest_val = int(max(list(values_during_years.items()), key=lambda x: int(x[0]))[1])

    increasing = (newest_val - oldest_val) / oldest_val * 100

    out = f"Paese: {para1} - Valore: {para2}\n"
    [out := out + f"{e:>10}" for e in values_during_years]
    out += "\n"
    [out := out + f"{e:>10}" for e in values_during_years.values()]
    out += f"\nDifferenza: {"+" if increasing > 0 else ""}{increasing:.2f}%\n\n"

    return out


def filter_by_year_value(year, value, co2):
    return {e["Paese"]: e[value] for e in co2 if e["Anno"] == year}


def maximum(para1, para2, co2):
    value_usage_in_year = filter_by_year_value(para1, para2, co2)

    min_usage = int(min(list(value_usage_in_year.items()), key=lambda x: int(x[1]))[1])
    max_usage = tuple(max(list(value_usage_in_year.items()), key=lambda x: int(x[1])))

    increasing = (int(max_usage[1]) - min_usage) / min_usage * 100

    out = f"Anno: {para1} - Valore: {para2}\n"
    out += f"Paese massimo: {max_usage[0]} ({max_usage[1]}, {"+" if increasing > 0 else ""}{increasing:.2f}% rispetto al minimo)\n\n"

    return out


def analize_queries(q, co2, output_path, csv_path):
    with open(output_path, "w") as out_file:
        output = f"Nome file: {csv_path}\n"

        years = [e["Anno"] for e in co2]
        first_year = min(years, key=lambda x: int(x))
        last_year = max(years, key=lambda x: int(x))
        countries = sorted(list(set(e["Paese"] for e in co2)))
        category = list(co2[0].keys())[2:]

        output += f"Anni monitorati: da {first_year} a {last_year}\nPaesi monitorati: "
        [output := output + f"{e} " for e in countries]
        output += "\nQuantita monitorate: "
        [output := output + f"{e} " for e in category]
        output += "\n\n"

        for e in q:
            if e[0] == "paese":
                output += country(e[1], e[2], co2)
            if e[0] == "massimo":
                output += maximum(e[1], e[2], co2)
        out_file.write(output[:-2])


def main():
    CSV_PATH = "./GCB2023.csv"
    QUERIES_PATH = "./queries.txt"
    OUTPUT_FILE = "./output.txt"

    try:
        CO2_report = get_stat_from_csv(CSV_PATH)
        queries = get_queries_from_file(QUERIES_PATH)

        analize_queries(queries, CO2_report, OUTPUT_FILE, CSV_PATH)
    except FileNotFoundError as err:
        print("File non trovato\n", err)
    except Exception as err:
        print("Errore nella computazione\n", err)


main()
