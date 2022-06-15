from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "2")
heading.pack()

#Save info function
def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()

    #Andmete salvestamine
    file = open("user.txt", "w")
    file.write("Firstname : " + firstname_info + "\n")
    file.write("Lastname : " + lastname_info + "\n")
    file.write("Age : " + str(age_info) + "\n")
    file.close()
    print("User", firstname_info, "has been registered successfully.")

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)

firstname_text = Label(text = "Firstname *",)
lastname_text =Label(text = "Lastname *",)
age_text = Label(text = "Age *",)
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 115)
age_text.place(x = 15, y = 160)

## Entry names
firstname = StringVar()
lastname = StringVar()
age = IntVar()

## Entry fields
firstname_entry = Entry(textvariable= firstname)
lastname_entry = Entry(textvariable= lastname)
age_entry = Entry(textvariable= age)

## Entry field placement on the screen..
firstname_entry.place(x= 15, y = 90)
lastname_entry.place(x= 15, y = 135)
age_entry.place(x= 15, y = 180)

## Button
register = Button(text = "Register", command = save_info)
register.place(x = 15, y = 205)


## Loop to make tkinter do his magic :)
screen.mainloop()
