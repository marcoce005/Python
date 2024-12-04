try:
    FILE_PATH = "dataset_albergo.txt"

    activity = ["alloggio", "conferenza", "cena"]
    tot_price_act = [0] * 3

    with open(FILE_PATH) as file:
        for line in file:
            data = line.split(";")
            tot_price_act[activity.index(data[1].lower())] += float(data[2])
            
    print("\nAttività e relativo utile totale:\n")
    [print(f"{e.capitalize():>20}", end="") for e in activity]
    print()
    [print(f"{e:19.2f}€", end="") for e in tot_price_act]
    
    
except FileNotFoundError:
    print(f"Il file '{FILE_PATH}' non esiste o non è presente in questa cartella.")
except:
    print("Errore nell'elaborazione del file controllare la correttezza dei dati.")
