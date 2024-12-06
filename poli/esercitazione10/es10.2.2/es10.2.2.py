# Creazione di un file classes.txt con almeno 15 corsi elencati.

# class_codes = [
#     "CSC1",
#     "CSC2",
#     "CSC46",
#     "CSC151",
#     "MTH121",
#     "PHY101",
#     "ENG201",
#     "BIO111",
#     "CHEM121",
#     "HIS210",
#     "ART130",
#     "PHIL101",
#     "PSY200",
#     "ECON102",
#     "STAT310",
# ]

# with open("./classes.txt", "w") as classes_file:
#     classes_file.write("\n".join(class_codes))


# creazione file per ogni corso

# from random import randint, choice

# marks = [
#     "A+", "A", "A-",
#     "B+", "B", "B-",
#     "C+", "C", "C-",
#     "D+", "D", "D-"
# ]

# with open("./classes.txt", "r") as in_file:
#     for line in in_file:
#         with open(f"{str(line).rstrip()}.txt", "w") as out_file:
#             for i in range(randint(0, 100)):
#                 out_file.write(f"{i + 10000} {choice(marks)}\n")

id_student = input("Inserire l'ID dello stundete:\t")

print(f"Student ID:\t{id_student}\n")

with open("./classes.txt", "r") as classes:
    for c in classes:
        with open(f"{c.rstrip()}.txt", "r") as students:
            file = students.read().split()
            if id_student in file:
                print(f"{c.rstrip()} {file[file.index(id_student) + 1]}")
