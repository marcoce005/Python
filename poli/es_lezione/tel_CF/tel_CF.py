def create_CF_tel(path):
    d = {}
    with open(path, "r") as file:
        for line in file:
            line_splitted = line.rstrip().split(":")
            (
                d[line_splitted[1]].append(line_splitted[0])
                if line_splitted[1] in d.keys()
                else d.update({line_splitted[1]: [line_splitted[0]]})
            )
    return d


def sort_num_tel(d):
    for k, v in d.items():
        d[k] = sorted(v)


def sort_name_in_alphabetic(d):
    return dict(sorted(list(d.items()), key=lambda x: x[0]))


CF_tel = create_CF_tel("./num_tel.txt")

sort_num_tel(CF_tel)

CF_tel = sort_name_in_alphabetic(CF_tel)

print(CF_tel)
