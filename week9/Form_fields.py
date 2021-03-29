#Author Lauri Putkonen
#Check 4 different fields of a feedback form before it can be submitted.
#E.g user has to give age, telephone number, homepage url, email and/or other
#information and those values are checked (contents cannot be empty, either).

from tkinter import *
from tkinter import messagebox
import re

def invalidInput(information, example):
    messagebox.showerror("Missing information", information + " has invalid value or field is empty\n\n" +
                        "Example: " + example)

def emptyField():
    messagebox.showerror("Empty field", "All fields must be filled")

def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = telephone_entry.get()
    homepage = homepage_entry.get()
    feedback = textbox.get("1.0", "end-1c")

    if not name or not age or not phone or not feedback:
        emptyField()
    elif not re.match("^[a-z A-Z]+$", name):
        invalidInput("Name", "Jack Smith")
    elif not re.match("^\d{1,3}$", age):
        invalidInput("Age", "52 - Value in years")
    elif not re.match("^\+{0,1}[0-9 \-]{1,}$", phone):
        invalidInput("Phone", "040-4520540")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        invalidInput("Email", "example@address.com")
    elif not re.match("^[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", homepage):
        invalidInput("Homepage", "www.example.ee")
    else:
        messagebox.showinfo("Submitted", "Thank you for the feedback")

window = Tk()
window.title("Feedback Form")
window.geometry("480x320")
window.resizable(False, False)

topic_label = Label(window, text="Fill the form", pady=15, font="Garamond 18 bold")
nameLabel = Label(window, text="Name", font="garamond 12", width=10, anchor="e")
email_label = Label(window, text="Email", font="garamond 12", width=10, anchor="e")
age_label = Label(window, text="Age", font="garamond 12", width=10, anchor="e")
telephone_label = Label(window, text="Phone", font="garamond 12", width=10, anchor="e")
homepage_label = Label(window, text="Homepage", font="garamond 12", width=10, anchor="e")
textbox_label = Label(window, text="Feedback", font="garamond 12", width=10, anchor="e")


name_entry = Entry(width=40)
age_entry = Entry(width=40)
telephone_entry = Entry(width=40)
email_entry = Entry(width=40)
homepage_entry = Entry(width=40)
textbox = Text(window, height=5, width=40)


topic_label.grid(row=0, column=1)

nameLabel.grid(row=1, column=0)
name_entry.grid(row=1, column=1)

age_label.grid(row=2, column=0)
age_entry.grid(row=2, column=1)

telephone_label.grid(row=3, column=0)
telephone_entry.grid(row=3, column=1)

email_label.grid(row=4, column=0)
email_entry.grid(row=4, column=1)

homepage_label.grid(row=5, column=0)
homepage_entry.grid(row=5, column=1)

textbox_label.grid(row=6, column=0)
textbox.grid(row=6, column=1)

submit_button = Button(text="Submit", padx=50, command=submit)
submit_button.grid(row=7, column=1)

window.mainloop()
