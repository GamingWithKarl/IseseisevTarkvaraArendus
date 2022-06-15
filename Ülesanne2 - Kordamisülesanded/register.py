from tkinter import *

def register_user():
    #Poroolide ja nime saamine
    username_info = username.get()
    password_info = password.get()

    #Kasutajainfo faili panemine (for safe keeping)
    file = open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    #Kustutab kirjutatu.
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    #Kui registeerimine õnnestus, antakse see kasutajale teada.
    Label(screen1, text = "Registratsioon õnnestus! ", fg = "green", font = ("calibri", 11 )).pack()

def register():
    #Luuakse uus window registeerimiseks.
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Registeerimine")
    screen1.geometry("300x250")

    #Kasutajainfo
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    #Nupud ja tekst registeerimiseks. Samuti ka tekstiväli parooli ja nime sisesetamiseks,
    Label(screen1, text = "Palun sisestage kasutajadetailid siia: ").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Kasutajanimi : ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Parool : ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    #Nupu kuvamine ekraanile.
    Button(screen1, text = "Registeerimine", width = 10, height = 1, command = register_user).pack()



def login():
    #Logimisüsteem (praegu ei kasutata registeeritud kasutaja informatsiooni.
    print("Login session started!")

def main_screen():
    #Ekraani seaded.
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 0.1 (Early Alpha)")
    Label(text = "Notes 0.1 (Early Alpha)", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()

    #Nupud logimiseks ning registeerimiseks
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Registeerimine", height = "2", width = "30", command = register).pack()

    #Ekraan pantakse loopi (et kasutada saaks ilusti)
    screen.mainloop()

#Käivitatakse programm. ;p
main_screen()

