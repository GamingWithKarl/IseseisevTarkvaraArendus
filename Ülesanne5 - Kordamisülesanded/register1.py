# Importitakse tkinter ja os
from tkinter import *
import os

#Defineeritakse kolm delete funksiooni.
def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()

#Login success ekraan, kui parool ka kasutajanimi on õige.
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = delete2).pack()

#Ekraan, kui parool pole õige.
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Not Recognised")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command = delete3).pack()

#Ekraan, kui kasutajanime ei leita.
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User Not Found")
    screen5.geometry("150x100")
    Label(screen5, text = "Username was not found").pack()
    Button(screen5, text = "OK", command = delete4).pack()

#Kasutaja registeerimine.
def register_user():
    #Poroolide ja nime saamine
    username_info = username.get()
    password_info = password.get()

    #Kasutajainfo faili panemine (for safe keeping)
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    #Kustutab kirjutatu.
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    #Kui registeerimine õnnestus, antakse see kasutajale teada.
    Label(screen1, text = "Registratsioon õnnestus! ", fg = "green", font = ("calibri", 11)).pack()

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

    #Globaliseeritakse username_entry ja password_entry
    global username_entry1
    global password_entry1

    # Username ja password entry nupud
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Parool : ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    #Nupu kuvamine ekraanile.
    Button(screen1, text = "Registeerimine", width = 10, height = 1, command = register_user).pack()

# Sisselogimisasju
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    #Failist vaatamine, kas parool ja kasutajanimi on õige.
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()



# Defineeritakse login funksioon.
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    # Label kasutajadetailisde sisestamiseks
    Label(screen2, text = "Palun sisestage kasutajadetailid siia logimiseks: ").pack()
    Label(screen2, text = "").pack()

    # Globaliseeritakse username_verify ja password_verify
    global username_verify
    global password_verify

    # Username ja password _verify pantakse StringVar()
    username_verify = StringVar()
    password_verify = StringVar()

    # Globaliseeritakse username_entry1 ja password_entry1
    global username_entry1
    global password_entry1

    #Kasutajanimi ja parooliväli
    Label(screen2, text = "Kasutajanimi : ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Parool : ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()


    #Login nupud
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

#Main ekraan
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

