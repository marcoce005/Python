from string import punctuation
from random import randint, choice


def read_file_replace_all_punctuation(path):
    with open(path) as file:
        s = file.read()
        for e in punctuation:
            if e in s:
                s = s.replace(e, "")
    return s.lower().split()


def count_lemmi(text):
    d = {}
    # length = len(text.split("\n"))
    # for j, line in enumerate(text.split("\n")):
    #     print(f"Traing:\t{j / length * 100:.2f} %")
    #     if line != "\n":
    #         line = line.split()
    #         for i in range(len(line) - 1):
    #             if f"{line[i]} {line[i + 1]}" not in d:
    #                 d[f"{line[i]} {line[i + 1]}"] = text.count(
    #                     f"{line[i]} {line[i + 1]}"
    #                 )

    for i in range(len(text) - 1):
        if text[i] not in d:
            d[text[i]] = {}
        if text[i + 1] in d[text[i]]:
            d[text[i]][text[i + 1]] += 1
        else:
            d[text[i]][text[i + 1]] = 1

    return d


def next_word(d):
    return choice(sorted(d.items(), key=lambda x: x[1], reverse=True)[:5])[0]


def random_word(l):
    return choice(list(l.keys()))


def generate_text(l, s):
    if s not in l:
        s = random_word(l)

    text = ""
    for _ in range(randint(5, 50)):
        s = next_word(l[s])
        text += s + " "

    return text


def main():
    FILE_PATH = "./promessisposi.txt"

    text = read_file_replace_all_punctuation(FILE_PATH)
    lemmi = count_lemmi(text)

    start_word = input("\nInserire la parola di inizio:\t").lower()
    while start_word != "":
        print(generate_text(lemmi, start_word) + "\n")
        start_word = input("\nInserire la parola di inizio:\t").lower()


main()
