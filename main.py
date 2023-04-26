from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
COLORS = "#070A52"
filename = "/Users/Godgive Computer/PycharmProjects/day 29 projects/logo.png"
window = Tk() 
window.title("Password Generator")
window.config(padx=50, pady=50, bg=COLORS)
##canvas
logo = PhotoImage(file=filename)
canvas = Canvas(width=200, height=200, bg=COLORS, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0) 
##labels
website_label = Label(text="Website:", bg=COLORS, fg="White")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=COLORS, fg="White")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", fg="White", bg=COLORS)
pass_label.grid(column=0, row=3)
##textboxes
web_text = Entry(width=50)
web_text.grid(column=1, row=1, columnspan=2)
web_text.focus()

email_text = Entry(width=50)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, string="wick92633@gmail.com")

pass_text = Entry(width=32)
pass_text.grid(column=1, row=3)

##buttons
gen_pass = Button(text="Generate Password", width=14, fg="White", bg=COLORS)
gen_pass.grid(column=2, row=3)

add_to_pass = Button(text="Add", width=42, fg="White", bg=COLORS)
add_to_pass.grid(column=1, row=4, columnspan=2)


window.mainloop()

