from tkinter import *

## bottoni = se li clicchi fanno qualcosa

c = 0
def click() :               ## per contare quante volte hai schiacciato il pulsante
    global c
    print ("\nHai cliccato il pulsante")
    c += 1

window = Tk()

foto = PhotoImage(file = '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/GUI/logo.png')

button = Button(window, 
                text = "Clicca", 
                command = click,        ## se premuto fa...
                font = ("Comic Sans", 22), 
                fg = "#00FF00", 
                bg = "black", 
                activeforeground = "yellow",   ## per il colore del pulsante quando ci passi sopra o lo clicchi
                activebackground = 'blue', 
                state = ACTIVE,           ## se è disabilitato il pulsante non si può premere
                image = foto,               ## inserire una foto insieme al testo
                compound = 'top')

button.pack()   ## come per la label lo adatta in base alla dimensione

window.mainloop()

print ("\nHai schiacciato il pulsante:\t volte", c)