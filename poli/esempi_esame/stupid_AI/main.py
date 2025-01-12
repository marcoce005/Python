import string, sys


def read_file_replace_all_punctuation(path):
    with open(path) as file:
        s = file.read()
        for e in string.punctuation:
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


def main():
    FILE_PATH = "./promessisposi.txt"

    text = read_file_replace_all_punctuation(FILE_PATH).lower()
    lemmi = count_lemmi(text)

    print(lemmi)


main()
