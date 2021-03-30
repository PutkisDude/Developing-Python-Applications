# Author Lauri Putkonen
# Give examples of using min 5 different even handlers.
# Give examples of some new controls that we you have not used before or that
# have not been presented on this guide.

# click mouse on canvas to draw dots/stars
# enter to canvas and exit to canvas to see useless print
# press space to clear all from canvas
# press 1-3 to change colors of dots
# hold 2nd or 3rd mouse button down to keep drawing

from tkinter import *
from tkinter.ttk import *

color = "yellow"

def clear(space):
    canvas.delete("all")

def draw(pos):
    global x, y
    x, y = pos.x, pos.y
    canvas.create_line(x, y, x+3, y+3, fill=color)


def changeColor(key):
    global color
    if key.char == '1':
        color = "white"
    elif key.char == '2':
        color = "yellow"
    elif key.char == '3':
        color = "red"
    else:
        color = "pink"

win = Tk()
win.title("Event handlers")
win.geometry("640x480")
win.resizable(False, False)

canvas = Canvas(win, height=480, width=635, bg="black")

canvas.bind("<Button-1>", draw) # Mouseclick event
win.bind("<B3-Motion>", draw) # Motion event
win.bind("<ButtonRelease>", lambda event: print("Button released")) # Release

canvas.bind("<Enter>", lambda event: print("Mouse in the canvas")) #Enter event
canvas.bind("<Leave>", lambda event: print("Mouse left the canvas")) # Leave event



win.bind("<Key>", changeColor) # Key event
win.bind("<space>", clear) # press space to remove all
canvas.pack()



win.mainloop()
