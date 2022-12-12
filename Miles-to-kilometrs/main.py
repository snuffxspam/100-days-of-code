from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    kim = miles * 1.609
    km_input.config(text=kim)

window = Tk()
window.title("Miles to kilometrs convert")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles = Label(text="miles")
miles.grid(column=2, row=0)

lable = Label(text="is equal to")
lable.grid(column=0, row=1)

km_input = Label(text="0")
km_input.grid(column=1, row=1)

km = Label(text="km")
km.grid(column=2, row=1)

button = Button(text="convert", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
