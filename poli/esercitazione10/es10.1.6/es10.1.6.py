def create_cyper(k):
    key_word = []
    for c in k.upper():
        key_word.append(c) if c not in key_word else None

    for i in range(90, 65, -1):
        key_word.append(chr(i)) if chr(i) not in key_word else None

    return key_word


def crypt():
    return


def decrypt():
    return


KEY = "FEATHER"

cyper = create_cyper(KEY)
