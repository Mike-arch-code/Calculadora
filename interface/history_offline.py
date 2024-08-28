from tkinter import ttk
from model import clear_historial
from model import input_bar_fuctions
import tkinter as tk
from model import save

conten_historial = False
historial_file_path = 'assets\\historial.txt'
def historial(container):
    try:
        global conten_historial
        global window
        window = ttk.Frame(container, borderwidth=1, relief='solid')
        s = ttk.Style()
        s.configure('my.TButton', font=('Arial', 12))
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)

        try:
            with open(historial_file_path, 'r') as file:
                historial_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            historial_list = []

        if len(historial_list) > 0:
            conten_historial = True

        if not conten_historial:
            ttk.Label(window, text="No hay historial").grid(column=0, row=0, sticky="nsew")
        else:
            for i, conten in enumerate(historial_list, start=1):
                ttk.Button(window, style='my.TButton', compound="center",command=lambda conten=conten: input_bar_fuctions.historial(conten),text=conten).grid(column=0, row=len(historial_list) - i, sticky="nsew")
                ttk.Button(window, style='my.TButton', compound="center",command=lambda i=i: clear_historial.clear_historial_item(i, historial_list),text="Delete").grid(column=1, row=len(historial_list) - i, sticky="nsew")
        return window
    except:
        pass

def actulice_historial():
    try:
        global conten_historial
        conten_historial = True

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        for widget in window.winfo_children():
            widget.destroy()
        try:
            with open(historial_file_path, 'r') as file:
                historial_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            historial_list = []

        for i, conten in enumerate(historial_list, start=1):
            ttk.Button(window, style='my.TButton', compound="center",command=lambda conten=conten: input_bar_fuctions.historial(conten),text=conten).grid(column=0, row=len(historial_list) - i, sticky="nsew")
            ttk.Button(window, style='my.TButton', compound="center",command=lambda i=i: clear_historial.clear_historial_item(i, historial_list),text="Delete").grid(column=1, row=len(historial_list) - i, sticky="nsew")
    except:
        pass
    

def subir_historial():

    window1 = tk.Tk()
    window1.title("Subir Historial")

    frame = ttk.Frame(window1, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    message = ttk.Label(frame, text="Desea subir el historial que se generó en local", font=("Arial", 12))
    message.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

    accept_button = ttk.Button(frame, text="Accept",command=lambda:save.save_offline_to_online(window1,True))
    accept_button.grid(row=1, column=0, pady=10)
    accept_button = ttk.Button(frame, text="Decline",command=lambda:save.save_offline_to_online(window1,False))
    accept_button.grid(row=1, column=2, pady=10)

    window1.columnconfigure(0, weight=1)
    window1.columnconfigure(2, weight=1)
    window1.rowconfigure(0, weight=1)
    window1.mainloop()