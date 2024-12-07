def print_mat(m):
    for r in m:
        print(*r)


def remove_double(k):
    l = []
    for c in k.replace("J", "I"):
        if c not in l:
            l.append(c)
    return l


def create_chiper(k):
    m = []
    n_ascii = 65
    cp_k = k[:]

    for r in range(5):
        l = []
        for i in range(5):
            if len(k) > 0:
                l.append(k[0])
                k.pop(0)
            else:
                while chr(n_ascii) in cp_k or chr(n_ascii) == "J":
                    n_ascii += 1
                l.append(chr(n_ascii))
                n_ascii += 1
        m.append(l)

    return m


def get_coordinate(v, m):
    for i, r in enumerate(m):
        if v in r:
            return i, r.index(v)


def convert(a, b, c):
    a_r, a_c = get_coordinate(a, c)
    b_r, b_c = get_coordinate(b, c)

    if a_r == b_r or a_c == b_c:
        return b, a
    return c[a_r][b_c], c[b_r][a_c]


def are_there_2_char(s):
    count = 0
    for c in s:
        if count == 2:
            return True
        if 65 <= ord(c.upper()) <= 90:
            count += 1
    return False


def get_couple(s):
    el = []
    i = 0
    pre = ""
    middle = ""

    if not are_there_2_char(s):
        return el, s, middle

    while len(el) != 2:
        if 65 <= ord(s[i].upper()) <= 90:
            el.append(s[i])
        else:
            if len(el) == 0:
                pre += s[i]
            else:
                middle += s[i]
        i += 1

    return el, pre, middle


def read_file(f, c):
    out = ""

    for line in f:
        line = line.replace("J", "I")
        line = line.replace("j", "i")
        l = ""
        i = 0
        while len(l) != len(line):
            if len(line[i:]) == 1:
                l += line[i:]
                i += 1
            else:
                el, pre, middle = get_couple(line[i:].upper())

                if len(el) == 0:
                    a = b = ""
                else:
                    a, b = convert(el[0], el[1], c)

                l += pre + a + middle + b
                i += len(el) + len(pre) + len(middle)

        l = list(l)
        for i in range(len(l)):
            if str(line[i]).islower():
                l[i] = l[i].lower()

        out += "".join(l)
    return out


KEY = "PLAYFAIR"

mod = input(
    "Selezionare la modalità:\n - [c] per cifrare un file\n - [d] per decifrare un file\n-->"
).lower()

while mod != "c" and mod != "d":
    print("\n\nModalità inesistene, Riprovare:\n")
    mod = input(
        "Selezionare la modalità:\n - [c] per cifrare un file\n - [d] per decifrare un file\n-->"
    ).lower()

file_path = input("\nInserire il percorso del file\n-->")

chiper = create_chiper(remove_double(KEY.upper()))

try:
    with open(file_path) as in_file:
        output = read_file(in_file, chiper)

    with open("chiper_text.txt" if mod == "c" else "plain_text.txt", "w") as out_file:
        out_file.write(output)

except Exception as err:
    print(f"{err}\nRiprovare.")
