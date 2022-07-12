from tkinter import *

window = Tk()
window.title("Celsius to Fahrenheit Converter")
window.config(height=500, width=500)
window.config(padx=20, pady=20)

label = Label()
label.config(text="                 ")
label.grid(column=0, row=0)
label.config(padx=5, pady=5)

entry = Entry(width=10)
entry.grid(column=1, row=0)

celsius = Label()
celsius.config(text="° Celsius")
celsius.grid(column=2, row=0)
celsius.config(padx=5, pady=5)

is_equal_to = Label()
is_equal_to.config(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=5, pady=5)

fahrenheit_value = Label()
fahrenheit_value.config(text=0)
fahrenheit_value.grid(column=1, row=1)
fahrenheit_value.config(padx=5, pady=5)

fahrenheit = Label()
fahrenheit.config(text="° Fahrenheit")
fahrenheit.grid(column=2, row=1)
fahrenheit.config(padx=5, pady=5)


def calculate():
    celsius_value = float(entry.get())
    frh = (celsius_value * 9/5) + 32
    fahrenheit_value.config(text=frh)


calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()
