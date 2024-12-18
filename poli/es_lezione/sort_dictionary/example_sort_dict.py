#   dobbiamo define la chiave di ordinamento
#   la chiave di ordinamento è una funzione

#   usiamo la libreria operator nello specifico il metodo itemgetter(param)

from operator import itemgetter


def sort_by_age(d):
    # d.sort(key=lambda x: x["age"])
    d.sort(key=itemgetter("age"))


def sort_by_age_and_name(d):
    d.sort(
        key=itemgetter("age", "name")
    )  # la sequenza degli argomenti è anche la sequenza di priorità di ordine


def max_of_age(l):
    return max(l, key=itemgetter("age"))


students = [
    {"name": "ciro", "age": 11},
    {"name": "gianni", "age": 13},
    {"name": "pluto", "age": 7},
    {"name": "mario", "age": 9},
    {"name": "pippo", "age": 22},
    {"name": "gianfraschio", "age": 9},
]

sort_by_age(students)

print(students)

sort_by_age_and_name(students)

print(students)

print(f"Older student:\t{max_of_age(students)}")
