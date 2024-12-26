import re


def clean_line(s):
    correct_characters = [str(i) for i in range(10)] + list("mul(,)")
    return "".join([c for c in s if c in correct_characters])


def read_file(path):
    with open(path) as file:
        return [clean_line(line) for line in file]
    return result


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
        [int(e) for e in s[i + 4 :].split(")")[0].split(",")]
        for i in range(len(s) - 3)
        if s[i : i + 3] == "mul" and check_correct_args(s[i + 3 : i + 12])
    ]


def mul_args(l):
    return [e[0] * e[1] for e in l]


def print_result(l):
    tot = 0
    for line in l:
        # for i, arg in enumerate(line):
        # print(*arg, sep="*", end=" + " if i != len(line) - 1 else " = ")
        tot += sum(mul_args(line))
        # print(sum(mul_args(line)))
    return tot


def main():
    FILE_PATH = "./test.txt"

    try:
        clean_file = read_file(FILE_PATH)

        pattern = r"mul\((\d+),(\d+)\)"
        matches = [[(int(e[0]), int(e[1])) for e in  re.findall(pattern, line)] for line in clean_file]

        result = [e[0] * e[1] for line in matches for e in line]
        
        print(sum(result))
        # print(matches)

        arguments = [extract_args(line) for line in clean_file]

        # print(arguments)
        
        # print(arguments == matches)

        add_all = print_result(arguments)
        
        print(f"\n\nAdd all = {add_all}")

    except FileNotFoundError:
        print("File not found")
        return
    except Exception as err:
        print("Something gone wrong\n", err)
        return


main()
