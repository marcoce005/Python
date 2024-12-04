with open("./input.txt") as in_file:
    with open("./output.txt", "w") as out_file:
        for i, line in enumerate(in_file):
            out_file.write(f"/* {i + 1} */{line}")
