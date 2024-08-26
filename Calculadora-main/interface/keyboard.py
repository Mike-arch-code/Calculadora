import tkinter as tk
from tkinter import TclError, ttk
from interface import basic_butons
from interface import trigonometricas

def create_keyboard_frame(container):

    frame = ttk.Frame(container)
    frame.grid(row=0, column=0, sticky="nsew")
    
    frame.columnconfigure(0,weight=1)
    frame.rowconfigure(0,weight=1)
    
    notebook = ttk.Notebook(frame)

    
    tab1 = basic_butons.basic(frame)
    tab2 = trigonometricas.basic(frame)
    
    tab1.columnconfigure(0, weight=1)
    tab1.rowconfigure(0, weight=1)
    tab2.columnconfigure(0, weight=1)
    tab2.rowconfigure(0, weight=1)
    
    
    notebook.add(tab1,text="123")
    notebook.add(tab2,text="sin")
    
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[5, 5], font=("Arial", 12))
    
    notebook.grid(column=0,row=0, sticky="nsew")
    
    


    return frame