def check_IBAN(iban):
    if len(iban) > 30 or len(iban) < 15:
        print("\nIBAN length incorrect")
        return False

    iban = (iban[4:] + iban[0:4]).upper()
    iban = "".join([str(ord(e) - 55) if e.isalpha() else e for e in iban])

    return int(iban) % 97 == 1


iban = input("Enter IBAN:\t").replace(" ", "")

print(f"Is valid:\t{check_IBAN(iban)}")
