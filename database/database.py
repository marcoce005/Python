mod_file = input("Devi modificare il file? yes[y]-no[n](stampa file di testo)-> ")
status='y'
r=1
if mod_file == 'y':
    #copio da fine a txt di appoggio
    r=0
    fine_open=open("testi/fine.txt","r").read()
    appo_open=open("testi/appo.txt","w")
    appo_open.write(fine_open)
    appo_open.close()
    add_text=open("testi/data.txt","w",encoding='utf8')
    while status=='y':
        text=input("Inserisci testo-> ")
        add_text.write("| "+text)
        add_text.write('\n')
        status=input( "Devi ancora inserirne? yes[y]-no[n]-> ")
    add_text.close()
else:
    open_text=open("testi/fine.txt","r").read()
    print("FILE DI TESTO:\n")
    print(open_text)
open_1=open("testi/appo.txt","r").read()
open_2=open("testi/data.txt","r").read()
open_3=open("testi/fine.txt", "w")
open_3.write(open_1+open_2)
open_3.close()
pulizia=input("Vuoi ripulire il file? yes[y]-no[n]-> ")
open_to_remember=open("testi/fine.txt","r").read()
remember=open("testi/ricorda.txt","w")
remember.write(open_to_remember)
remember.close()
#pulisce file txt
if pulizia=='y':
    open_to_remember=open("test/fine.txt","r").read()
    remember=open("testi/ricorda.txt","w")
    remember.write(open_to_remember)
    remember.close()
    open_4=open("testi/fine.txt", "w")
    open_4.write("")
    open_4.close()
if r==0:
    print("FILE DI TESTO:\n\n")
    open_3=open("testi/fine.txt", "r").read()
    print(open_3)
chiudi=input("Premi invio per chiudere il programma...")