from tkinter import *
from tkinter import ttk

expression = ""
history = []


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        history.append(f"{expression} = {total}")
        history_listbox.insert(END, f"{expression} = {total}")
        history_listbox.see(END)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title("Gaming Calculator")
    gui.geometry("500x500")

    main_frame = Frame(gui, bg="black")
    main_frame.pack(expand=True, fill="both", padx=10, pady=10)

    history_frame = Frame(main_frame, bg="black")
    history_frame.pack(fill="both", expand=True, pady=(0, 10))

    scrollbar = ttk.Scrollbar(history_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    history_listbox = Listbox(
        history_frame,
        yscrollcommand=scrollbar.set,
        bg="black",
        fg="red",
        font=("Arial", 14),
        height=6,
        width=40,
    )
    history_listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=history_listbox.yview)

    input_frame = Frame(main_frame, bg="black")
    input_frame.pack(fill="x", pady=(0, 10))

    equation = StringVar()
    expression_field = Entry(
        input_frame, textvariable=equation, font=("Arial", 14), justify="right"
    )
    expression_field.pack(fill="x", ipady=8)

    button_frame = Frame(main_frame, bg="black")
    button_frame.pack(fill="x", pady=(0, 10))

    button_style = {
        "font": ("Arial", 12),
        "height": 2,
        "width": 7,
        "relief": "raised",
        "borderwidth": 3,
    }

    button1 = Button(
        button_frame,
        text="1",
        fg="black",
        bg="red",
        command=lambda: press(1),
        **button_style,
    )
    button1.grid(row=0, column=0, padx=2, pady=2)

    button2 = Button(
        button_frame,
        text="2",
        fg="black",
        bg="red",
        command=lambda: press(2),
        **button_style,
    )
    button2.grid(row=0, column=1, padx=2, pady=2)

    button3 = Button(
        button_frame,
        text="3",
        fg="black",
        bg="red",
        command=lambda: press(3),
        **button_style,
    )
    button3.grid(row=0, column=2, padx=2, pady=2)

    button4 = Button(
        button_frame,
        text="4",
        fg="black",
        bg="red",
        command=lambda: press(4),
        **button_style,
    )
    button4.grid(row=1, column=0, padx=2, pady=2)

    button5 = Button(
        button_frame,
        text="5",
        fg="black",
        bg="red",
        command=lambda: press(5),
        **button_style,
    )
    button5.grid(row=1, column=1, padx=2, pady=2)

    button6 = Button(
        button_frame,
        text="6",
        fg="black",
        bg="red",
        command=lambda: press(6),
        **button_style,
    )
    button6.grid(row=1, column=2, padx=2, pady=2)

    button7 = Button(
        button_frame,
        text="7",
        fg="black",
        bg="red",
        command=lambda: press(7),
        **button_style,
    )
    button7.grid(row=2, column=0, padx=2, pady=2)

    button8 = Button(
        button_frame,
        text="8",
        fg="black",
        bg="red",
        command=lambda: press(8),
        **button_style,
    )
    button8.grid(row=2, column=1, padx=2, pady=2)

    button9 = Button(
        button_frame,
        text="9",
        fg="black",
        bg="red",
        command=lambda: press(9),
        **button_style,
    )
    button9.grid(row=2, column=2, padx=2, pady=2)

    button0 = Button(
        button_frame,
        text="0",
        fg="black",
        bg="red",
        command=lambda: press(0),
        **button_style,
    )
    button0.grid(row=3, column=0, padx=2, pady=2)

    plus = Button(
        button_frame,
        text="+",
        fg="black",
        bg="red",
        command=lambda: press("+"),
        **button_style,
    )
    plus.grid(row=0, column=3, padx=2, pady=2)

    minus = Button(
        button_frame,
        text="-",
        fg="black",
        bg="red",
        command=lambda: press("-"),
        **button_style,
    )
    minus.grid(row=1, column=3, padx=2, pady=2)

    multiply = Button(
        button_frame,
        text="×",
        fg="black",
        bg="red",
        command=lambda: press("*"),
        **button_style,
    )
    multiply.grid(row=2, column=3, padx=2, pady=2)

    divide = Button(
        button_frame,
        text="÷",
        fg="black",
        bg="red",
        command=lambda: press("/"),
        **button_style,
    )
    divide.grid(row=3, column=3, padx=2, pady=2)

    equal = Button(
        button_frame, text="=", fg="black", bg="red", command=equalpress, **button_style
    )
    equal.grid(row=3, column=2, padx=2, pady=2)

    clear = Button(
        button_frame, text="C", fg="black", bg="red", command=clear, **button_style
    )
    clear.grid(row=3, column=1, padx=2, pady=2)

    gui.mainloop()
