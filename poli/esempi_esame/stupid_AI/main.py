from string import punctuation
from random import randint, choice


def read_file_replace_all_punctuation(path):
    with open(path) as file:
        s = file.read()
        for e in punctuation:
            if e in s:
                s = s.replace(e, "")
    return s


def count_lemmi(text):
    d = {}
    length = len(text.split("\n"))
    for j, line in enumerate(text.split("\n")):
        print(f"Traing:\t{j / length * 100:.2f} %")
        if line != "\n":
            line = line.split()
            for i in range(len(line) - 1):
                if f"{line[i]} {line[i + 1]}" not in d:
                    d[f"{line[i]} {line[i + 1]}"] = text.count(
                        f"{line[i]} {line[i + 1]}"
                    )

    return d


def filter_by_first_word(d, w):
    return dict(
        sorted(
            {k: v for k, v in d.items() if k.split()[0] == w}.items(),
            key=lambda x: x[1],
            reverse=True,
        )[:5]
    )


def random_word(l):
    return choice(list(l.keys())).split()[1]


def generate_text(l, s):
    lemmi_start_with_word = filter_by_first_word(l, s)

    text = ""
    for _ in range(randint(5, 50)):
        if len(lemmi_start_with_word) == 0:
            s = random_word(l)
            lemmi_start_with_word = filter_by_first_word(l, s)

        s = choice(list(lemmi_start_with_word.keys())).split()[1]
        text += s + " "
        lemmi_start_with_word = filter_by_first_word(l, s)

    return text


def main():
    FILE_PATH = "./promessisposi.txt"

    text = read_file_replace_all_punctuation(FILE_PATH).lower()
    lemmi = count_lemmi(text)

    start_word = input("\nInserire la parola di inizio:\t").lower()
    while start_word != "":
        print(generate_text(lemmi, start_word) + "\n")
        start_word = input("\nInserire la parola di inizio:\t").lower()


main()
