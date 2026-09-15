from tkinter import *
import requests



def get_quote():
    api = requests.get(url="https://api.kanye.rest")
    api.raise_for_status()
    api_text = api.json()
    api_text_ = api_text["quote"]
    canvas.itemconfig(quote_text ,text=api_text_)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="kanye-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quotes!", width=250, font=("Arial", 15, "bold"), fill="white")


canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye-quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)




window.mainloop()