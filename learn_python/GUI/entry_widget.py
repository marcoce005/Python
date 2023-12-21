from curses import window
from tkinter import *

## entry widgets = servono per far inserire all'utente un input

def invio() :
    nome = entry.get()      ## prende il valore
    print ("\nNome = " + nome)
    entry.config(state = DISABLED)      ## la disabiliti dopo aver inserito il nome

def canc() :
    entry.delete(0, END)        ## per cancellare tutto

def back() :
    entry.delete(len(entry.get())-1, END)     ## per cancellare l'ultimo carattere


window = Tk()

window.config(background = 'black')

entry = Entry(window, 
            font = ("Arial", 32),
            bg = 'black', 
            fg = 'white', 
            bd = 1,
            show = "*")     ## per le password non farle vedere

#entry.insert(0, "Nome.....")        ## per mettere già qualcosa
entry.pack(side = LEFT)

pulsante_invio = Button(window, 
                        text = "INVIO",
                        font = ('Calibri', 22), 
                        command = invio,
                        bg = '#00FF00', 
                        fg = 'black',
                        bd = 1)
pulsante_invio.pack(side = RIGHT)

pulsante_canc = Button(window, 
                        text = "CANC",
                        font = ('Calibri', 22), 
                        command = canc,
                        bg = 'red', 
                        fg = 'black',
                        bd = 1)
pulsante_canc.pack(side = RIGHT)

pulsante_backspace = Button(window, 
                        text = "BACK",
                        font = ('Calibri', 22), 
                        command = back,
                        bg = 'orange', 
                        fg = 'black',
                        bd = 1)
pulsante_backspace.pack(side = RIGHT)

window.mainloop()