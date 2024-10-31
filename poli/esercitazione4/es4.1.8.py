n = input("Inserire un numero intero:\t")

pre = None
copy = ""
while n != "":
    n = int(n)
    copy += "" if str(n) in copy else (str(n) + " " if n == pre else "")
    print(f"Duplicati:\t{copy}")
    pre = n
    n = input("\nInserire un numero intero:\t")
