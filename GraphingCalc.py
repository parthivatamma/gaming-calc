from tkinter import *
from tkinter import messagebox
import itertools

tk = Tk()
tk.title("Graphing Calculator")
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

COLORS = ["blue", "red", "green", "purple", "orange", "brown", "pink", "cyan"]
color_cycle = itertools.cycle(COLORS)

canvas.create_line(250, 0, 250, 500, dash=(5,))
canvas.create_line(0, 250, 500, 250, dash=(5,))


def point(x, y, color):
    shiftedxval = x + 250
    shiftedyval = 250 - y
    canvas.create_oval(shiftedxval, shiftedyval, shiftedxval, shiftedyval, fill=color)


def drawLine(m, b):
    current_color = next(color_cycle)
    for x in range(-250, 250):
        y = m * x + b
        point(x, y, current_color)


def plot_another():
    try:
        user_slope_val = int(input("Enter slope: "))
        user_y_int_val = int(input("Enter y intercept: "))
        drawLine(user_slope_val, user_y_int_val)

        answer = input("Do you want to plot another line? (yes/no): ").lower()
        if answer == "yes":
            plot_another()
        else:
            print("Thanks for using the Graphing Calculator!")
    except ValueError:
        print("Please enter valid numbers for slope and y-intercept")
        plot_another()


plot_another()

tk.mainloop()
