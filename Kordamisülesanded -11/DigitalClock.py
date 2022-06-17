#Kordamisülesanded 11 fail btw.

#Importib vajalikud asjad
from tkinter import Tk
from tkinter import Label
import time

#Ekraani sätted.
master = Tk()
master.title("Digital Clock")

#Saab aja õiges formaadis.
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text = timeVar)
    clock.after(200, get_time())

#Saab kella ekraanile kuvatud.
clock = Label(master, font=("Calibri",90), bg = "grey", fg = "white")
clock.pack()

#Funktsiooni käivitab.
get_time()

#Loop
master.mainloop()

