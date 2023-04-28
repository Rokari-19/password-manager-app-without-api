from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []
nl = random.randint(8, 10)
nn = random.randint(2, 4)
ns = random.randint(2, 4)
def Generate_pass():
    global password
    for character in range(nl):
        random_letter = random.choice(letters)
        password += random_letter

    for character in range(nn):
        random_number = random.choice(numbers)
        password += random_number

    for character in range(ns):
        random_symbol = random.choice(symbols)
        password += random_symbol

    # print(password)   
    random.shuffle(password)
    # print(password)
    new_password = ""
    for char in password:
        new_password += char
    pass_text.insert(0, string=new_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    if len(web_text.get()) == 0 or len(pass_text.get()) == 0:
        messagebox.showinfo(title="Blank Fields", message="Please Do Not Leave Any Fields Empty")
    else: 
        is_ok = messagebox.askokcancel(title=web_text.get(), message=f"Are the details you provided correct?\n{web_text.get()} | {email_text.get()} | {pass_text.get()}")
        
        if is_ok:
            with open("datafile.txt", mode="a") as datafile:
                datafile.write(f"{web_text.get()} | {email_text.get()} | {pass_text.get()}\n")
                web_text.delete(0, END)
                pass_text.delete(0, END)


    # ---------------------------- UI SETUP ------------------------------- #
COLORS = "#070A52"
filename = "/Users/Godgive Computer/PycharmProjects/day 29 projects/logo.png"
window = Tk() 
window.title("Password Generator")
window.config(padx=50, pady=50, bg=COLORS)
#canvas
logo = PhotoImage(file=filename)
canvas = Canvas(width=200, height=200, bg=COLORS, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0) 
#labels
website_label = Label(text="Website:", bg=COLORS, fg="White")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=COLORS, fg="White")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", fg="White", bg=COLORS)
pass_label.grid(column=0, row=3)
#textboxes
web_text = Entry(width=50)
web_text.grid(column=1, row=1, columnspan=2)
web_text.focus()
str_website = web_text.__str__()

email_text = Entry(width=50)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, string="wick92633@gmail.com")
str_email = email_text.__str__()

pass_text = Entry(width=32)
pass_text.grid(column=1, row=3)
str_pass = pass_text.__str__()


#buttons
gen_pass = Button(text="Generate Password", width=14, fg="White", bg=COLORS, command=Generate_pass)
gen_pass.grid(column=2, row=3)

add_to_pass = Button(text="Add", width=42, fg="White", bg=COLORS, command=save_pass)
add_to_pass.grid(column=1, row=4, columnspan=2)


window.mainloop()

