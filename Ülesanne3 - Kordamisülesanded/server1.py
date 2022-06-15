import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print("This is your host: " + host)
print("Waiting for any incoming connections...")
conn, addr = s.accept()
print(addr, "Has connected to the server... ")

# From this point starts file transfer
filename = input(str("Please enter the filename of the file: "))
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully... ")

