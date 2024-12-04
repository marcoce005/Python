file_path = input("Inserire i nomi dei file separati da una virgola:\t").split(",")
word = input("Inserire la parola da cercare:\t")

print("\n\nFrasi in cui compaiono:\n\n")

for e in file_path:
    with open(e) as file:
        for line in file:
            if word in line:
                print(f"{e}:\t{line[:-1]}")
    print()
