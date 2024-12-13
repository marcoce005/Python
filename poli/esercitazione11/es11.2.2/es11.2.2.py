def get_genetic_code():
    d = {}
    with open("./codice_genetico.csv", "r") as file:
        for line in file:
            line = line.split(",", 1)

            for code in line[1].replace('"', "").split(","):
                code = code.strip()

                if code in d.keys():
                    d[code].append(line[0].strip())
                else:
                    d[code] = [line[0].strip()]
    return d


def get_start_stop_codes(g):
    start = []
    stop = []
    for k, v in g.items():
        start.append(k) if "start" in v else None
        stop.append(k) if "stop" in v else None

    return start, stop


def find_max_index(s, e):
    if s.find(e) == -1:
        return -1
    else:
        l = [s.find(e)]
        while s[l[-1] + 1 :].find(e) != -1:
            l.append(l[-1] + s[l[-1] + 1 :].find(e) + 1)
        return l[-1]


def find_start_stop_position(s, g):
    start, stop = get_start_stop_codes(g)

    start_occurence = [s.find(e) for e in start]
    stop_occurence = [find_max_index(s, e) for e in stop]

    return (
        -1
        if start_occurence == [-1] * len(start)
        else min([e for e in start_occurence if e != -1])
    ), (-1 if stop_occurence == [-1] * len(stop) else max(stop_occurence))


def decode_genetic_code(seq, g):
    start, stop = find_start_stop_position(seq, g)

    if start > stop or start * stop < 0 or start * stop == 1:
        return -1
    else:
        seq = seq[start:stop]
        decoded = ""

        for i in range(0, len(seq) - 2, 3):
            if seq[i : i + 3] not in g.keys():
                return -1

            possible = g[seq[i : i + 3]]
            decoded += [e for e in possible if e != "start" or e != "stop"][0]
        decoded += "stop"
    return decoded


genetic_code = get_genetic_code()

sequence = input(
    "Inserire una sequenza di nucleotidi [default = 'GUAUGCACGUGACUUUCCUCAUGAGCUGAU']:\t"
).upper()
sequence = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU" if sequence == "" else sequence

protein = decode_genetic_code(sequence, genetic_code)

if protein == -1:
    print("\n\nCatena inserita non è corretta, riprovare")
else:
    print(f"La catena proteica è la sequente:\t{protein}")
