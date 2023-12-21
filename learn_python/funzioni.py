## funzioni = eseguono il loro contenuto solo quando vengo chiamate


def hello(name) :               ## funzione tra () si passa un valore dal main
    print ("hello! " + name)
    print ("ciao")

hello("Pippo")
hello("Pluto")

name = input("\nInserire il nome:\t")   
hello(name)                             ## il numero di oggetti passati deve esse uguale nella chiamata e nella funzione