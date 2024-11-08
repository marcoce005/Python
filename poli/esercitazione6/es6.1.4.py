def profit(years, money, percent):
    return [money := money * (1 + (percent / 100)) for i in range(years)][-1]

print(f"Investendo 1000€ per 10 anni a interesse 5% ottengo:\t{profit(10, 1000, 5):.2f}€")