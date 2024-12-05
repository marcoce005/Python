try:
    n = input("Inserire un numero reale:\t")
    l = []

    while n != "":
        l.append(float(n))
        n = input("Inserire un numero reale:\t")

except Exception as e:
    print(f"{e}\nRiprova sarai più fortunato:")
    
    n = input("Inserire un numero reale:\t")
    while n != "":
        l.append(float(n))
        n = input("Inserire un numero reale:\t")
        
print(f"\n\nSomma dei numeri inseriti:\t{sum(l)}")