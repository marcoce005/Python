str1 = input("Inserire una stringa:\t")
str2 = input("Inserire un'altra stringa:\t")

set_str1 = set(list(str1))
set_str2 = set(list(str2))

print(f"\n\nCaratteri in entrambe le stringhe:\t{set_str1.intersection(set_str2)}")

print(f"\nCaratteri in srt1 ma non in str2:\t{set_str1.difference(set_str2)}")

print(f"\nCaratteri in srt2 ma non in str1:\t{set_str2.difference(set_str1)}")

lower_alphas = {chr(i) for i in range(97, 122)}

print(
    f"\nLettere che non compaiono in una delle 2 stringhe:\t{lower_alphas.difference(set_str1)}"
)
