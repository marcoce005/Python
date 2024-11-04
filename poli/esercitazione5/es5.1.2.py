s = input("Inserire il nome di una nazione in francese:\t").lower()

male_exception = ["belize", "cambodge", "mexique", "mozambique", "zaire", "zimbabwe"]

if s[0] in "aeiou":
    print("L'", end=" ")
elif s in male_exception or s[-1] == "e":
    print("Le", end=" ")
elif s.endswith("s"):
    print("Les", end=" ")
elif s[-1] in "aiou":
    print("La", end=" ")
else:
    print("Paese non trovato.")
    exit(1)

print(s)
