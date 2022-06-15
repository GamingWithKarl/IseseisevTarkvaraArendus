import smtplib

sender_email = "#BLANKSENDEREMAIL#" # Siia lisa saatja e-mail.
rec_email = "#BLACKRECEMAIL" # Siia lisa saaja e-mail.
password = input(str("Please input your password :")) #Siia lisa saatja e-maili parool
message = "Hey, this was sent using python!" #Kirja sõnum

server = smtplib.SMTP("smtp.gmail.com", 587) #Kasutab smtp.gmail.com serverit.
server.starttls()
server.login(sender_email, password)    #Kasutab login credentiale.
print("Login success") #Prindim login successful.

server.sendmail(sender_email, rec_email, message)   #Saadab maili saajale.
print("Email has been sent to ", rec_email)
