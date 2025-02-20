def count_occurence(path):
    d = {}
    with open(path) as in_file:
        for line in in_file:
            [
                d.update({c: d[c] + 1}) if c in d else d.update({c: 1})
                for c in line.rstrip().lower()
            ]
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


def print_output(d):
    [print(f"{k} -> {v}") for k, v in d.items()]


FILE_PATH = "./input.txt"
occunrence = count_occurence(FILE_PATH)
print_output(occunrence)
