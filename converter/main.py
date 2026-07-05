from tkinter import *

window = Tk()
window.title("KM to Ml converter")
window.minsize(width=200, height=110)

label = Label(text="KM")
label.config(text="KM")
label.pack()

def converter():
    km = float(miles_input.get())
    ml = km/1.609
    kilometer_result_label.config(text=f"{ml}")

miles_input = Entry()
miles_input.pack()

is_equal = Label(text='is equal to')
is_equal.pack()

kilometer_result_label = Label(text="0")
kilometer_result_label.pack()

kilometer_label = Label(text="Km")
kilometer_label.pack()

calculate_button = Button(text="Calculate", command=converter)
calculate_button.pack()

window.mainloop()
