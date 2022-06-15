### Importid ###
import socket
import sys
import time

### Programmi alustamine

s = socket.socket()
host = input(str("Palun sisestage serveri hostname: ")) ### Küsib serveri hostname'i.
port = 8080 ### Kõik toimib port 8080 peal.
s.connect((host,port)) ### Ühendatakse host ning port serveriga.
print("Ühendatud chat serveriga...") ### Antakse teada, et sai ühendatud kirjutamisserveriga.

#Kirjutamine teistele...
while True:
    #Kirja saamine serverilt.
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode() ### Kiri konvertitakse bitidest tähtedeks.
    print("Server : ", incoming_message) ### Kirja saamine serveri masinalt ning selle kuvamine...
    print("")

    #Kirja saatmine serverile.
    message = input(str(">> ")) ### Kirja saatmise väli
    message = message.encode() ### Muudab kirja bitideks.
    s.send(message) ### Kirja saatmine serverile.
    print("Kiri on saadetud...")
    print("")

