import tkinter as tk
from tkinter import TclError, ttk
from model import autentication
def login():
    
    global name
    global error

    window = tk.Tk()
    window.title("Calculadora Grafica")
    window.minsize(300,200)  

    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=2)
    window.rowconfigure(0,weight=1)
    window.rowconfigure(1,weight=1)
    window.rowconfigure(2,weight=1)
    window.rowconfigure(3,weight=1)
    

    ttk.Label(window, text="Username:").grid(row=0, column=0, sticky="ew")
    usuario = ttk.Entry(window)
    usuario.grid(row=0, column=1, sticky="ew")


    ttk.Label(window, text="Password:").grid(row=1, column=0, padx=5,sticky="ew")
    paswword = ttk.Entry(window)
    paswword.grid(row=1, column=1, sticky="ew")
    
    
    ttk.Button(window, text="Ingreso",command=lambda:autentication.autentication(usuario.get(),paswword.get(),window)).grid(row=2, column=0, columnspan=2, pady=10)

    error = ttk.Label(window)
    error.grid(row=3, column=0,sticky="ew",columnspan=2)

    window.mainloop()
    
    
    return autentication.value