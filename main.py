from tkinter import *
import tkinter.messagebox
from PASSWORD import passwords
import json
import pyperclip


def password_generate():
    a = passwords()
    pyperclip.copy(a)
    entry_3.delete(0, END)
    entry_3.insert(END, string=a)


def save_data():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {website: {"email": email, "password": password}}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo("Oops!", "Don't Leave any empty field")
    else:

        ask_yes = tkinter.messagebox.askokcancel("Submit Form",
                                                 f"You Entered: \n\nWebsite: {website}\n\nEmail: {email}\n\nPassword: {password}\n\nYou want to save this")
        if ask_yes:
            try:
                with open("password.jason", mode="r") as file:
                    data = json.load(file)
            except ValueError:
                with open("password.jason", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("password.jason", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_1.delete(0, END)
                entry_2.delete(0, END)
                entry_3.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website:")
label_1.grid(row=1, column=0)

entry_1 = Entry(width=36)
entry_1.grid(row=1, column=1)
entry_1.focus()

label_2 = Label(text="Email/Username:")
label_2.grid(row=2, column=0)

entry_2 = Entry(width=36)
entry_2.grid(column=1, row=2)

label_3 = Label(text="Password")
label_3.grid(row=3, column=0)

entry_3 = Entry(width=36)
entry_3.grid(row=3, column=1)

button_1 = Button(text="Generate Password", width=31, command=password_generate)
button_1.grid(row=4, column=1)
button_2 = Button(text="Add", width=31, command=save_data)
button_2.grid(row=5, column=1)


def search():
    with open("password.jason", mode="r") as file:
        data = json.load(file)
    try:
        website = entry_1.get()
        email = data[website]["email"]
        password = data[website]["password"]
        pyperclip.copy(password)
        tkinter.messagebox.showinfo("Found!", f"Your Email : {email}\n\n Password: {password}")
    except KeyError:
        tkinter.messagebox.showinfo("Opps!", "Details Not Found")


button_3 = Button(text="Search", command=search)
button_3.grid(row=1, column=2)

window.mainloop()
