s = input("Inserire una stringa:\t")

[print(s[-(i + 1)], end="") for i in range(len(s))]

print("\n\n")

[print(s[-(i + 1)], end="") for i in range(len(s)) if s[-(i + 1)].isupper()]
