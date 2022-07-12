from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(height=500, width=500)
window.config(padx=20, pady=20)

label = Label()
label.config(text="                 ")
label.grid(column=0, row=0)
label.config(padx=5, pady=5)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles = Label()
miles.config(text="Mile/s")
miles.grid(column=2, row=0)
miles.config(padx=5, pady=5)

is_equal_to = Label()
is_equal_to.config(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=5, pady=5)

km_value = Label()
km_value.config(text=0)
km_value.grid(column=1, row=1)
km_value.config(padx=5, pady=5)

km = Label()
km.config(text="Kilometer/s")
km.grid(column=2, row=1)
km.config(padx=5, pady=5)


def calculate():
    miles_value = float(entry.get())
    kilometer = miles_value * 1.609
    km_value.config(text=kilometer)


calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()
