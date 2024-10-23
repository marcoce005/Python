s = input("Inserire stringa:\t")

print(f"\n\n'{s}', is alpha:\t\t{s.isalpha()}")
print(f"'{s}', is upper:\t\t{s.isupper()}")
print(f"'{s}', is lower:\t\t{s.islower()}")
print(f"'{s}', is numeric:\t\t{s.isdigit()}")
print(f"'{s}', is alp/num:\t\t{s.isalnum()}")
print(f"'{s}', start with upper:\t{s[0].isupper()}")
print(f"'{s}', end with point:\t\t{s.endswith('.')}")
