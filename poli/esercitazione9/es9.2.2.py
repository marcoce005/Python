game = 1
print(f"\n\n\t\tGAME {game}\n")

n = input("Inserire la parola iniziale [* per terminare la partita]:\t")
words = [n]
pre = n[-2:]

while n != "*":
    n = input(
        f"Inserire la parola che inizi per '{pre}' [* per terminare la partita]:\t"
    )

    if n[:2] != pre or n in words:
        game += 1
        print(
            "Parola già inserita"
            if n in words
            else "La parola non inizia con la corretta sillaba"
        )
        print("\n\t\tGAME OVER")

        print(f"\n\n\t\tGAME {game}\n")
        n = input("Inserire la parola iniziale [* per terminare la partita]:\t")
        words = [n]
        pre = n[-2:]
    else:
        words.append(n)
        pre = n[-2:]
