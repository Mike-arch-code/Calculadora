import tkinter as tk
from tkinter import TclError, ttk
from model import ingreso
def log():

    window = tk.Tk()
    window.title("Calculadora Grafica")
    window.minsize(300,200)  

    window.columnconfigure(0,weight=1)
    window.rowconfigure(0,weight=1)
    window.rowconfigure(1,weight=1)
    window.rowconfigure(2,weight=1)
    

    login_button = ttk.Button(window,text="Login",command=lambda:ingreso.ingreso(1,window))
    login_button.grid(row=0, column=0, sticky="nsew")

    register_button = ttk.Button(window, text="Register",command=lambda:ingreso.ingreso(2,window))
    register_button.grid(row=1, column=0, sticky="nsew")

    offline_button = ttk.Button(window, text="Offline Mode",command=lambda:ingreso.ingreso(3,window))
    offline_button.grid(row=2, column=0, sticky="nsew")

    window.mainloop()
    
    return ingreso.x