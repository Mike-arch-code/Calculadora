import tkinter as tk
from tkinter import ttk
from model import volver


def internet():

    window = tk.Tk()
    window.title("Internet Connection")

    window.overrideredirect(True)

    frame = ttk.Frame(window, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    message = ttk.Label(frame, text="Se perdió la conexión a Internet.\nPor favor, valida y vuelve a ingresar.", font=("Arial", 12))
    message.grid(row=0, column=0, padx=10, pady=10)

    accept_button = ttk.Button(frame, text="Accept",command=lambda:volver.volver())
    accept_button.grid(row=1, column=0, pady=10)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.mainloop()
