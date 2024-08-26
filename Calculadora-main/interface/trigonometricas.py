from tkinter import TclError, ttk
from interface import crete_button

def basic(container):

    frame = ttk.Frame(container)
    style = ttk.Style()
    style.configure("Bold.TButton", font=("Segoe UI", 12, "bold"))

    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(1,weight=1)
    frame.columnconfigure(2,weight=1)
    frame.columnconfigure(3,weight=1)

    frame.rowconfigure(0,weight=1)
    frame.rowconfigure(1,weight=1)
    frame.rowconfigure(2,weight=1)
    frame.rowconfigure(3,weight=1)
    frame.rowconfigure(5,weight=1)

    data = [
        ["sin(", "cos(", "tan(", "*"],
        ["log(", "1/x", "√(", "/"],
        ["x^2", "(", ")", "+"],
        ["e", "π", "^", "-"]
    ]

    # Crear los botones en la cuadrícula
    for i in range(4):
        for n in range(4):
            crete_button.create_button(n, i, data[i][n], frame)

    crete_button.create_button_DELL(0,5,"DELL",frame)
    crete_button.create_button_ANS(2,5,"ENTER",frame)
    return frame