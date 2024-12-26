import re


def check_correct_args(s):
    if s[0] != "(":
        return False

    if len(s[1:].split(")")) == 1:
        return False

    arguments = s[1:].split(")")[0].split(",")

    if len(arguments) != 2:
        return False

    for e in arguments:
        if not e.isdigit():
            return False
    return True


def extract_args(s):
    return [
        tuple([int(e) for e in s[i + 4 :].split(")")[0].split(",")])
        for i in range(len(s) - 3)
        if s[i : i + 3] == "mul" and check_correct_args(s[i + 3 : i + 12])
    ]


def mul_args(l):
    return [e[0] * e[1] for e in l]


def print_result(l):
    tot = 0
    for line in l:
        tot += sum(mul_args(line))
    return tot


def main():
    FILE_PATH = "./test.txt"

    try:
        file = open(FILE_PATH, "r").read().split("\n")

        # pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        # matches = re.findall(pattern, "".join(file))
        # result = [int(x) * int(y) for x, y in matches]
        # print(sum(result))

        arguments = [extract_args(line) for line in file]

        add_all = print_result(arguments)

        print(f"Add all = {add_all}")

    except FileNotFoundError:
        print("File not found")
        return
    except Exception as err:
        print("Something gone wrong\n", err)
        return


main()
