from tkinter import * 

## labels = area di una finestra che contiene scritte e/o immagini

window = Tk()

## nella label si setta tutto dal testo al font al colore del testo, background ecc...

foto = PhotoImage(file = '/home/marco/Documenti/marco/github_privato/MarcoCellini/Python/learn_python/GUI/logo.png')

label = Label(window,
                text = "Ciao sono Pippo",               ## testo
                font = ('Calibrì', 32, 'bold'),         ## font
                fg = 'blue',                    ## color text
                bg = 'yellow',                          ## color background
                relief = RAISED,                   ## mette il bordo
                bd = 8,                 ## dimensione del bordo
                padx = 20,          ## distanza dal bordo X e Y
                pady = 20, 
                image = foto,               ## inserire la foto e la sua posizione
                compound = 'bottom')                               

label.pack()       ## serve per visualizzarolo al centro e si adatta in base al grandezza della label

#label.place(x = 0, y = 0)           ## secondo le coordinate che vuoi tu

window.mainloop()