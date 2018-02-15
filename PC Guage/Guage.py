import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.title("PC Guage")

w = Canvas(window, width=500, height=600)
w.pack()


blue = w.create_rectangle(50, 25, 150, 550, fill="blue")
red = w.create_rectangle(200, 25, 300, 550, fill="red")
green = w.create_rectangle(350, 25, 450, 550, fill="green")


def increase_blue(rect = blue, x=30):
    x0, y0, x1, y1 = w.coords(rect)
    y0 = y0 - x
    w.coords(rect, x0, y0, x1, y1) # change later

b1 = ttk.Button(window, text="Increase Blue", command=increase_blue)
b1.pack()

blue_value = tk.StringVar()
blue_entered = ttk.Entry(window, width=12, textvariable=blue_value)
blue_entered.pack()




def reduce_blue(rect=blue, x = blue_entered.get()):
    print("Value is {}".format(x))
    int(x)
    x0, y0, x1, y1 = w.coords(rect)
    y0 = y0 + x
    print(y0)
    if y0 < 550:
        w.coords(rect, x0, y0, x1, y1)
    elif y0 > 550:
        w.coords(rect, x0, y1, x1, y1)

b1 = ttk.Button(window, text="Reduce Blue", command=reduce_blue)
b1.pack()


#red_value = tk.StringVar()
#red_entered = ttk.Entry(window, width=12, textvariable=red_value)
#red_entered.pack()



window.mainloop()