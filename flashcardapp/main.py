BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox


window = Tk()
window.config(padx=50, pady=50)
img_bg = PhotoImage(file="flashcardapp/images/card_back.png")
img_ft = PhotoImage(file="flashcardapp/images/card_front.png")
cross = PhotoImage(file="flashcardapp/images/right.png")
check = PhotoImage(file="flashcardapp/images/wrong.png")



window.title("Flash lang")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=img_bg)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


button_c = Button(image=cross, highlightthickness=0)
button_c.grid(row=1, column=0)

button_r = Button(image=check, highlightthickness=0)
button_r.grid(row=1, column=1)

window.mainloop()