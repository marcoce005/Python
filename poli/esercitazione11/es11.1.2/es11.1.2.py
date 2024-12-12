from operator import itemgetter


def clean_word(s):
    return "".join([c for c in s if c.isalpha()])


def print_occurence(d):
    print(f"\n\nParola --> ricorrenze\n")
    for k, v in d.items():
        print(f"{k} --> {v}")


def filter_dict(d):
    article = [
        # Articoli determinativi
        "il",
        "lo",
        "l'",
        "la",
        "i",
        "gli",
        "le",
        # Articoli indeterminativi
        "un",
        "uno",
        "una",
        "un'",
        # Articoli partitivi
        "del",
        "dello",
        "dell'",
        "della",
        "dei",
        "degli",
        "delle",
        # Preposizioni semplici
        "di",
        "a",
        "da",
        "in",
        "con",
        "su",
        "per",
        "tra",
        "fra",
        # Preposizioni articolate
        "al",
        "allo",
        "all'",
        "alla",
        "ai",
        "agli",
        "alle",
        "dal",
        "dallo",
        "dall'",
        "dalla",
        "dai",
        "dagli",
        "dalle",
        "nel",
        "nello",
        "nell'",
        "nella",
        "nei",
        "negli",
        "nelle",
        "sul",
        "sullo",
        "sull'",
        "sulla",
        "sui",
        "sugli",
        "sulle",
        # Congiunzioni coordinanti
        "e",
        "anche",
        "inoltre",
        "né...né",
        "ma",
        "però",
        "tuttavia",
        "invece",
        "bensì",
        "o",
        "oppure",
        "ovvero",
        "altrimenti",
        "dunque",
        "quindi",
        "pertanto",
        "perciò",
        "cioè",
        "infatti",
        "ossia",
        # Congiunzioni subordinanti
        "perché",
        "poiché",
        "siccome",
        "dato che",
        "quando",
        "mentre",
        "appena",
        "finché",
        "dopo che",
        "affinché",
        "in modo che",
        "così che",
        "tanto che",
        "talmente che",
        "se",
        "qualora",
        "purché",
        "a patto che",
        "anche se",
        "benché",
        "sebbene",
        "nonostante",
        "come",
        "quanto",
        "più di",
        "meno di",
        "mentre",
        "laddove",
    ]
    return {k: v for k, v in d.items() if k not in article}


def get_first_five(d):
    # return dict(sorted(d.items(), key=itemgetter("value"), reverse=True)[:5])
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:5])


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


word_occurence = filter_dict(word_occurence)

print_occurence(get_first_five(word_occurence))
