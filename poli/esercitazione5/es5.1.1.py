PIN = "1234"

tries = 1

n = input("Inserire il codice:\t")
while n != PIN and tries < 3:
    print("Your PIN is incorrect, retry.")
    n = input("Inserire il codice:\t")
    tries += 1

print("Your bank card is blocked" if tries == 3 and n != PIN else "Your PIN is correct")
