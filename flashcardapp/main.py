BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
import pandas as pd

window = Tk()
window.config(padx=50, pady=50)
img_bg = PhotoImage(file="flashcardapp/images/card_back.png")
img_ft = PhotoImage(file="flashcardapp/images/card_front.png")
cross = PhotoImage(file="flashcardapp/images/right.png")
check = PhotoImage(file="flashcardapp/images/wrong.png")
df = pd.read_csv('flashcardapp/data/data.csv')
wordss = df.to_dict(orient="records")


i = 0
def word_f():
    global i
    listword = wordss[i]
    new_word_f = str(listword['French'])
    i += 1
    return new_word_f
x = 0
def word_e():
    global x
    listword = wordss[i]
    new_word_e = str(listword['English'])
    x += 1
    return new_word_e

    

window.title("Flash lang")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)      
card_img = canvas.create_image(400, 263, image=img_bg)
card_tittle = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text=word_e(), font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

def default():
    canvas.itemconfig(card_img, image=img_bg)
    canvas.itemconfig(card_tittle, text="English")
    canvas.itemconfig(card_text, text= word_e())

def switch():
    canvas.itemconfig(card_img, image=img_ft)
    canvas.itemconfig(card_tittle, text="French")
    canvas.itemconfig(card_text, text=word_f())
    window.after(2000, default)


button_c = Button(image=cross, highlightthickness=0, command=switch, )
button_c.grid(row=1, column=0)

button_r = Button(image=check, highlightthickness=0, command=switch, )
button_r.grid(row=1, column=1)


window.mainloop()