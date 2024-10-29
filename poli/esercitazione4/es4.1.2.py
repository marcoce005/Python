s = input("Inserire stringa:\t")

uppers = "".join([e for e in s if e.isupper()])

evens = "".join([e for i, e in enumerate(s) if i % 2 == 0])

replaced = "".join(["_" if e in "aeiou" else e for e in s.lower()])

nums = 0
[nums := nums + 1 for e in s if e.isalnum()]

print(f"Maiuscole:\t{uppers}")
print(f"Pari:\t{evens}")
print(f"Rimpiazzo:\t{replaced}")

[print(f"{e} --> {i} index") for i, e in enumerate(s) if e in "aeiou"]
