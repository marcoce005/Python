print("Si accettano solo caratteri 'A', 'C', 'T', 'G'")

long_s = input("Inserire la seguenza lunga di 20 caratteri:\t")
short_s = input("Inserire la sequenza corta di 3 caratteri:\t")

print(f"Sequenza corta in lunga:\t{short_s in long_s}")

if short_s in long_s:
    print(f"Ricorre all'indece:\t{long_s.find(short_s)}")
    print(f"Ricorre {long_s.count(short_s)} volte")
