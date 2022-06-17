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