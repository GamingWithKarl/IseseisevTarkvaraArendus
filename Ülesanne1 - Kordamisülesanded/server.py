### Importid ###
import socket

### Programmi alustamine

s = socket.socket()
host = socket.gethostname() ### Annab arvuti või arvutite hostname'id.
print("Server alustab hostil : ", host) ### Hosti kuvamine kasutajale
port = 8080 ### Pordi kasutamine serveriks
s.bind((host,port))

print("")
print("Server on hosti ja pordiga seotud edukalt!") ### Annab teada, et port ja host on toimiv.
print("")
print("Server ootab ühendusi serveriga......")
s.listen(1) ### Kuulab, kuni saab ühendusi.
conn, addr = s.accept() ###Aksepteerib ühendused
print(addr, "On nüüd ühendatud serverige ning on online...") ### Näitab kasutajale, et server ja client on ühendatud edukalt.
print("")

while True:
    #Kirja saatmine client'ile.
    message = input(str(">> ")) ### Tekstiväli, kuhu teksti kirjutatakse.
    message = message.encode() ### Muudab kirja bitideks.
    conn.send(message) ### Saadab kirja client masinale.
    print("Kiri on saadetud...")
    print("")

    #Kirja saamine clientilt
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode() ### Kiri konvertitakse bitidest tähtedeks.
    print("Client : ", incoming_message) ### Kirja saamine client masinalt ja selle kuvamine.
    print("")
