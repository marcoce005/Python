def create_cyper(k):
    key_word = []
    for c in k.upper():
        key_word.append(c) if c not in key_word else None

    for i in range(90, 65, -1):
        key_word.append(chr(i)) if chr(i) not in key_word else None

    return key_word


def crypt(f, cy):
    return [
        "".join(l)
        for l in [
            [
                (
                    cy[ord(c.upper()) - 65]
                    if c.isupper()
                    else (
                        cy[ord(c.upper()) - 65].lower()
                        if 65 <= ord(c.upper()) <= 90
                        else c
                    )
                )
                for c in line
            ]
            for line in f
        ]
    ]


def decrypt(f, cy):
    return [
        "".join(l)
        for l in [
            [
                (
                    chr(cy.index(c) + 65)
                    if c.isupper()
                    else (
                        chr(cy.index(c.upper()) + 65).lower()
                        if 65 <= ord(c.upper()) <= 90
                        else c
                    )
                )
                for c in line
            ]
            for line in f
        ]
    ]


KEY = "FEATHER"

cyper = create_cyper(KEY)

try:
    mod = input(
        "Selezionare la modilità:\n[C] per cifrare un file\n[D] per decifrare un file\n-->"
    ).upper()

    while mod != "C" and mod != "D":
        print("Modalità inesistene, Riprovare:\n")
        mod = input(
            "Selezionare la modilità:\n[C] per cifrare un file\n[D] per decifrare un file\n-->"
        ).upper()

    file_path = input(
        f"\nSelezionare il file da {"cifrare" if mod == "C" else "decifrare"} [es. ciro.txt]\n-->"
    )

    with open(file_path, "r") as in_file:
        out = crypt(in_file, cyper) if mod == "C" else decrypt(in_file, cyper)

    with open("chyper_text.txt" if mod == "C" else "plain_text.txt", "w") as out_file:
        for line in out:
            out_file.write(line)

except Exception as err:
    print(err)
