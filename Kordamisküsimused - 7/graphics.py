from tkinter import *

#Run funksioon (prindib nime ekraanile)
def run():
    name1 = name_storage.get()
    print(name1)
    name.delete(0, END)

#Ekraani seaded.
screen = Tk()
screen.title("Graphics Program - Karl Karulin")
screen.geometry("500x500")

#Ekraanile asjade kuvamine
welcome_text = Label(text = "Welcome to our first graphics program ", fg = "red", bg = "yellow")
welcome_text.pack()

#Nupp
click_me = Button(text = "Click me :)", fg = "red", bg = "yellow", command = run)
click_me.place(x = 20, y = 30) # Panin ise paremasse kohta ;)

#Name storage ning nimi ise ;)
name_storage = StringVar()
name = Entry(textvariable= name_storage)
name.pack()

#Ekraani loop (et midagi ekraanile kuvataks)
screen.mainloop()


#Dokumentatsioon

#Mida programm teeb?
#Programm kuvab ekraanile tkinteri abiga teksti koos nupuga, kuhu kasutaja peab klickima, samuti ka koht, kuhu saab ise asju sisse kirjutada.
#Seda koodi saab ka muuta ning luua väga erinevaid programmide menüüsid lihtsaks kasutamiseks.

#Mida võiks edasi arendada?
#Oma menuu suhtes saaks väga palju erinevaid asju teha (nt lisada taustapilt, nupud mängude jaoks nt, registeerimisalad ja palju muud).
#Tkinteri abiga on see vähemalt lihtne ning ei võta väga kaua aega. 