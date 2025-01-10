import random


def get_questions_from_file(path):
    d = {}
    with open(path, "r") as file:
        question = file.readline().rstrip()
        while question != "":
            dif = int(file.readline().rstrip())
            correct = file.readline().rstrip()
            ans = [
                file.readline().rstrip(),
                file.readline().rstrip(),
                file.readline().rstrip(),
                correct,
            ]

            d[question] = {"difficult": dif, "correct": correct, "answers": ans}
            file.readline()
            question = file.readline().rstrip()
    return d


def get_most_diffult(d):
    return max(d.items(), key=lambda x: x[1]["difficult"])[1]["difficult"]


def get_question_by_difficult(d, n):
    l = list({k: v for k, v in d.items() if v["difficult"] == n}.items())
    random.shuffle(l)
    return l[0]


def save_in_file(path, n, p):
    with open(path, "a") as out_file:
        out_file.write(f"{n} {p}\n")


def main():
    QUESTIONS_PATH = "./domande.txt"
    OUTPUT_FILE = "./punti.txt"

    name = input("Inserisci il tuo nickname:\t")

    try:
        questions = get_questions_from_file(QUESTIONS_PATH)
    except FileNotFoundError as err:
        print("file non trovato\n", err)
        return

    max_dif = get_most_diffult(questions)

    for i in range(max_dif + 1):
        quest = get_question_by_difficult(questions, i)

        print(quest[0])

        answers = quest[1]["answers"]
        random.shuffle(answers)

        print(*answers, sep="\n")

        try:
            user_ans = int(input("Inserire la risposta [1-2-3-4]:\t"))

            if user_ans <= 0:
                raise ()

            if quest[1]["correct"] == answers[user_ans - 1]:
                print("Risposta corretta!\n")
            else:
                print(
                    f"Risposta sbagliata! La risposta corretta era: {answers.index(quest[1]["correct"]) + 1}"
                )
                break
        except Exception:
            print("Input non valido riprovare. ")
            return

    print(f"\nHai totalizzato {i} punti!")

    save_in_file(OUTPUT_FILE, name, i)


main()
