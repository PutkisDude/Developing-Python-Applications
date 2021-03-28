#Author Lauri Putkonen

from tkinter import *

def clear():
    text.delete(0, END)


def click(button):
    in_calc = text.get()
    text.delete(0, END)
    text.insert(0, str(in_calc) + str(button))


def button_equal():
    equal = eval(text.get()) # I decided use eval(), tho its not recommended because it's not safe
    text.delete(0, END)
    text.insert(0, equal)

def removeLast():
    removed = text.get()
    removed = removed[:-1]
    text.delete(0, END)
    text.insert(0, removed)

window = Tk()
window.title("Crappy Calculator")
window.resizable(False, False)

text = Entry(window, borderwidth=2)
text.grid(row=0, column=0, columnspan=4, pady=20)

# Number buttons
button_1 = Button(window, padx=25, pady=25, text="1", command=lambda: click(1))
button_2 = Button(window, padx=25, pady=25, text="2", command=lambda: click(2))
button_3 = Button(window, padx=25, pady=25, text="3", command=lambda: click(3))
button_4 = Button(window, padx=25, pady=25, text="4", command=lambda: click(4))
button_5 = Button(window, padx=25, pady=25, text="5", command=lambda: click(5))
button_6 = Button(window, padx=25, pady=25, text="6", command=lambda: click(6))
button_7 = Button(window, padx=25, pady=25, text="7", command=lambda: click(7))
button_8 = Button(window, padx=25, pady=25, text="8", command=lambda: click(8))
button_9 = Button(window, padx=25, pady=25, text="9", command=lambda: click(9))
button_0 = Button(window, padx=25, pady=25, text="0", command=lambda: click(0))
# Symbol buttons etc
button_dot = Button(window, padx=25, pady=25, text=".", command=lambda: click("."))
button_plus = Button(window, padx=25, pady=25, text="+", command=lambda: click("+"))
button_minus = Button(window, padx=25, pady=25, text="-", command=lambda: click("-"))
button_divide = Button(window, padx=25, pady=25, text="/", command=lambda: click("/"))
button_multiple = Button(window, padx=25, pady=25, text="*", command=lambda: click("*"))
button_equal = Button(window, padx=25, pady=25, text="=", bg="green", command=button_equal)
button_clear = Button(window, padx=25, pady=5, text="Clear", command=clear)
button_undo = Button(window, padx=25, pady=5, text="Undo", command=removeLast)



#ADD Buttons - 1st row

button_undo.grid(row=1, column=0, columnspan=2)
button_clear.grid(row=1, column=2, columnspan=2)
#2nd row
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)
# 3rd row
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiple.grid(row=3, column=3)
# 4th row
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_minus.grid(row=4, column=3)
# 5th row
button_0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)
button_plus.grid(row=5, column=2)
button_equal.grid(row=5, column=3)


window.mainloop()
