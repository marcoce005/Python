s = input("Inserire la stringa:\t")

for i in range(len(s)):
    [print(s[i : j + 1]) for j in range(i, len(s))]
