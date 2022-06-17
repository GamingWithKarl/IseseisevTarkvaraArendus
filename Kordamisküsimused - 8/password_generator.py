import random

#Parooli characterid.
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!&$%^£*(')"

#Random password loop
while 1:

    #Küsitakse kasutajalt paroolide pikkuseid ning mitu parooli tahetakse.
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like: "))

    #Loop paroolide tegemiseks
    for x in range(0, password_count):

        #Parool storitakse sellesse stringi.
        password = ""

        #Loopitakse nii kaua, kuna jõutakse parooli pikkusele.
        for x in range(0, password_len):
            password_char = random.choice(chars) #Võtab suvalise characteri listist.
            password = password + password_char #Parool pantakse stringi.
        print("Here is your password: ", password) #Kuvatakse parool ekraanile.

#Dokumentatsioon.

#Mis on kasutusala?
#Kasutusalaks on turvaliste paroolide tegemine. See on sisse ka ühendatud näiteks Google Chrome'i, mis ise genereerib parooli ja salvestab selle sinu google'i kontole.
#See on palju turvalisem, kui igat parooli igas kohas kasutada.
#Samuti on see ka väga mugav kasutajale.

#Mida saaks edasi arendada?
# Lisada saaks rohkem erinevaid charactere, et oleks veel raskem paroole kätte saada.