from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    
    if sec < 10:
        sec = f"0{sec}"
    
    canvas.itemconfig(timer, text=f"{min}:{sec}")
    
    if count > 0:
        window.after(1000, count_down, count - 1)
    #else:
    #    check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    #    check_marks.grid(column=1, row=3)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomoder")
window.config(padx=250, pady=62.5, bg=YELLOW)


title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 20, "bold"), padx=20, highlightthickness=0)
title.grid(column=1, row=0 )

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100 , 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold") )
canvas.grid(column=1, row=1)



start = Button(text="Start", highlightthickness=0, command=start_timer )
reset = Button(text="Reset", highlightthickness=0)

start.grid(column=0, row=2)
reset.grid(column=2, row=2)


window.mainloop()