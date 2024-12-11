def clean_word(s):
    return "".join([c for c in s if c.isalpha()])


def print_occurence(d):
    print(f"\n\nParola --> ricorrenze\n")
    for k, v in d.items():
        print(f"{k} --> {v}")


path = input("Inserire il file da analizzare [default = input.txt]:\t")

path = "./input.txt" if path == "" else path

word_occurence = {}

with open(path) as file:
    for line in file:
        for word in line.split():
            word = clean_word(word)

            word_occurence[word] = (
                word_occurence[word] + 1 if word in word_occurence.keys() else 1
            )


print_occurence(word_occurence)
