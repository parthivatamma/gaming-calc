from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_line(250,0,250,500,dash=(5,))
canvas.create_line(0,250,500,250,dash=(5,))

def point(x,y):
    shiftedxval = x + 250
    shiftedyval = 250 - y
    canvas.create_oval(shiftedxval,shiftedyval,shiftedxval,shiftedyval, fill='blue')

def drawLine(m,b):
    for x in range (-250,250):
        y = m * x + b
        point(x,y)    

user_slope_val = int(input('Enter slope: '))
user_y_int_val = int(input('Enter y intercept: '))
drawLine(user_slope_val,user_y_int_val)
        
