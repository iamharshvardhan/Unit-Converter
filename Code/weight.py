from tkinter import *

window = Tk()
window.title("Kilogram to Pound Converter")
window.config(height=500, width=500)
window.config(padx=20, pady=20)

label = Label()
label.config(text="                 ")
label.grid(column=0, row=0)
label.config(padx=5, pady=5)

entry = Entry(width=10)
entry.grid(column=1, row=0)

pound = Label()
pound.config(text="Pound/s")
pound.grid(column=2, row=0)
pound.config(padx=5, pady=5)

is_equal_to = Label()
is_equal_to.config(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=5, pady=5)

kg_value = Label()
kg_value.config(text=0)
kg_value.grid(column=1, row=1)
kg_value.config(padx=5, pady=5)

kilogram = Label()
kilogram.config(text="Kilogram/s")
kilogram.grid(column=2, row=1)
kilogram.config(padx=5, pady=5)


def calculate():
    pds_value = float(entry.get())
    kg = pds_value * 1.6
    kg_value.config(text=kg)


calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()
