def get_bad_words():
    with open("./bad_words.txt", "r") as file:
        return {line.rstrip() for line in file}


def clean_word(s):
    return "".join([c for c in s if c.isalpha()])


def censor_only_alpha(s):
    return "".join(["*" if c.isalpha() else c for c in s])


def censor(path_file, banned_words):
    with open(path_file, "r") as in_file:
        with open("censored_text.txt", "w") as out_file:
            for line in [line.split(" ") for line in in_file]:
                for word in line:
                    print(
                        (
                            censor_only_alpha(word)
                            if clean_word(word) in banned_words
                            else word
                        ),
                        file=out_file,
                        end="" if "\n" in word else " ",
                    )


bad_words = get_bad_words()

path = input("Inserire il path del file da censurare [default = raw_text.txt]:\t")

path = "./raw_text.txt" if path == "" else path

censor(path, bad_words)
