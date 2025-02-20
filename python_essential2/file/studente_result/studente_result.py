class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, l):
        self.__line = l

    def __str__(self):
        return f"The line {self.__line} is corrupted."


class FileEmpty(StudentsDataException):
    def __str__(self):
        return "The file is empty."


def check_line(l, n):
    if len(l) != 3:
        raise (BadLine(n + 1))
    try:
        assert float(l[2])
    except:
        raise (BadLine(n + 1))


def get_from_file(path):
    d = {}
    with open(path) as in_file:
        for i, line in enumerate(in_file):
            line = line.rstrip().split()
            check_line(line, i)
            (
                d.update(
                    {f"{line[0]}-{line[1]}": d[f"{line[0]}-{line[1]}"] + float(line[2])}
                )
                if f"{line[0]}-{line[1]}" in d
                else d.update({f"{line[0]}-{line[1]}": float(line[2])})
            )
    return d

def print_output(d):
    [
        print(f"{k.split("-")[0]:10} {k.split("-")[1]:10} {v}")
        for k, v in sorted(d.items(), key=lambda x: x[0])
    ]


path = input("Insert the file path, with extension [.txt]:\t")

try:
    data = get_from_file(path)
    if data == {}:
        raise (FileEmpty)

    print_output(data)

except FileNotFoundError as err:
    print("Wrong path")
except FileEmpty as err:
    print(err)
except BadLine as err:
    print(err)
