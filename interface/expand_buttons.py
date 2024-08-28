from tkinter import TclError, ttk
from model import size_window

def expand_buttons(container):

    frame = ttk.Frame(container)
    style = ttk.Style()
    style.configure("Bold.TButton", font=("Helvetica", 12,"bold"))

    frame.columnconfigure(0,weight=1)
    frame.rowconfigure(0,weight=1)

    ttk.Button(frame,text=("Grafica"),style="Bold.TButton",command=lambda:size_window.grafic_size()).grid(column=0,row=0,sticky="nsew")
    
    frame.columnconfigure(1,weight=1)
    ttk.Button(frame,text=("Historial"),style="Bold.TButton",command=lambda:size_window.hitorial_size()).grid(column=1,row=0, sticky="nsew")

    return frame