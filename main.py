from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip as py
import json as js

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nl = randint(8, 10)
nn = randint(2, 4)
ns = randint(2, 4)


def Generate_pass():
    pass_text.delete(0, END)
    pass_letters = [choice(letters) for _ in range(nl)]
    pass_numbers = [choice(numbers) for _ in range(nn)]
    pass_sym = [choice(symbols) for _ in range(ns)]

    new_pass_list = pass_letters + pass_numbers + pass_sym
    shuffle(new_pass_list)
    new_password = "".join(new_pass_list)
    py.copy(new_password)
    pass_text.insert(0, string=new_password)


# ---------------------------- finding PASSWORD ------------------------------- #

def find_pass():
    website = web_text.get()
    try:
        with open("datafile.json") as datafile:
            data = js.load(datafile)
            if web_text.get() in data:
                messagebox.showinfo(title=web_text.get(), message=f"Email: {data[web_text.get()]['email']}\nPassword: {data[web_text.get()]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file created")


    # print(data)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    new_data = {
        web_text.get(): {
            "email": email_text.get(),
            "password": pass_text.get(),
        }
    }

    if len(web_text.get()) == 0 or len(pass_text.get()) == 0:
        messagebox.showinfo(title="Blank Fields", message="Please Do Not Leave Any Fields Empty")
    else:
        try:
            with open("datafile.json", mode="r") as datafile:
                # js.dump(new_data, datafile, indent=4)
                data = js.load(fp=datafile)
                data.update(new_data)
        except FileNotFoundError:
            with open("datafile.json", "w") as datafile:
                js.dump(new_data, datafile, indent=4)
        else:
            with open("datafile.json", "w") as datafile:
                js.dump(data, datafile, indent=4)
        finally:
            web_text.delete(0, END)
            pass_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

COLORS = "Black"
# change the filename based on your cloning/forking path
filename = "./Day 30/password-manager-app-without-api/image/logo.png"
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=COLORS)
# canvas
logo = PhotoImage(file=filename)
canvas = Canvas(width=200, height=200, bg=COLORS, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# labels
website_label = Label(text="Website:", bg=COLORS, fg="White")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=COLORS, fg="White")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", fg="White", bg=COLORS)
pass_label.grid(column=0, row=3)
# textboxes
web_text = Entry(width=32)
web_text.grid(column=1, row=1, )
web_text.focus()
str_website = web_text.__str__()

email_text = Entry(width=50)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, string="wick92633@gmail.com")
str_email = email_text.__str__()

pass_text = Entry(width=32)
pass_text.grid(column=1, row=3)
str_pass = pass_text.__str__()

# buttons
gen_pass = Button(text="Generate Password", width=14, fg="White", bg=COLORS, command=Generate_pass)
gen_pass.grid(column=2, row=3)

add_to_pass = Button(text="Add", width=42, fg="White", bg=COLORS, command=save_pass)
add_to_pass.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=14, fg="White", bg=COLORS, command=find_pass)
search_btn.grid(row=1, column=2)

window.mainloop()

#---------------------designed by rokarioss-----------------------#
