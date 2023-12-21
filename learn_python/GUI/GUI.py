from curses import window
from tkinter import *           

## widgets = elementi dell GUI bottoni, pulsanti, ecc...
## windows = server che contiene questi widgets

window = Tk()       ## instanzioare la finestra

window.geometry("420x420")      ## decidere la dimensione della finestra (si mette la risoluzione)

window.title("Pippo")       ## cambiare il nome alla finestra

icon = PhotoImage(file = '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/GUI/logo.png')
## per aggiungere un logo/icona alla finestra
window.iconphoto(True, icon)

window.config(background = "#c542f5")        ## cambiare il colore dello sfondo (con il nome o con il codice esadecimale)

window.mainloop()       ## visualizza la finestra