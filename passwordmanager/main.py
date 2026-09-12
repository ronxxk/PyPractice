from tkinter import *
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

all_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ]
all_chars = list(string.ascii_letters)
all_specials = list(string.punctuation)

def gene():
    pass_entry.delete(0, END)
    entr = ""
    passn = random.choices(all_nums, k = 4)
    passc = random.choices(all_chars, k = 4)
    passs = random.choices(all_specials, k = 4)
    entr += "".join(passn)
    entr += "".join(passc)
    entr += "".join(passs)
    shuffled_text = "".join(random.sample(entr, len(entr)))
    pass_entry.insert(0,(shuffled_text))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    ema = ema_entry.get()
    pas = pass_entry.get()
    with open("passwordmanager/output.txt", "a", encoding="utf-8") as data_file:
        data_file.write(f"{web} {ema} {pas}\n")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)
        web_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

window = Tk()
window.config(padx=50, pady=50)
img = PhotoImage(file="passwordmanager/logo.png")



window.title("Password Manager")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
ema_entry = Entry(width=35)
ema_entry.grid(row=2, column=1, columnspan=2)
ema_entry.insert(0, "zxc@dsa.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1,)


gener_button = Button(text="Generate", width=11, command=gene)
gener_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()