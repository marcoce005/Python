def discount(prices, is_pet):
    return is_pet.count(True) > 0 and len(is_pet) - is_pet.count(True) >= 5


prices = [float(input("Inserire il prezzo [reale] (0 per terminare l'inserimento):\t"))]
are_pets = [input("Inserire Y-N se è o meno un animale:\t").upper() == "Y"]

while prices[-1] != 0:
    prices.append(
        float(
            input("\n\nInserire il prezzo [reale] (0 per terminare l'inserimento):\t")
        )
    )
    are_pets.append(input("Inserire Y-N se è o meno un animale:\t").upper() == "Y")


prices.pop()
are_pets.pop()

d = discount(prices, are_pets)
print(
    f"\n{'Hai diritto allo sconto del 20%' if d else 'Non ha diritto allo sconto'}\nPrezzo da pagare:\t{sum(prices) - (sum(prices) * 0.2) if d else sum(prices)}€"
)
