import tkinter as tk
from tkinter import TclError, ttk
from model import add_usser
from model import volver

add_active = False

def register():

    global error
    global add_active

    window = tk.Tk()
    window.title("Calculadora Grafica")
    window.minsize(300,200)  

    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=2)
    window.rowconfigure(0,weight=1)
    window.rowconfigure(1,weight=1)
    window.rowconfigure(2,weight=1)
    window.rowconfigure(3,weight=1)
    window.rowconfigure(4,weight=1)
    

    ttk.Label(window, text="Username:").grid(row=0, column=0, sticky="ew")
    usuario = ttk.Entry(window)
    usuario.grid(row=0, column=1, sticky="ew")


    ttk.Label(window, text="Password:").grid(row=1, column=0,sticky="ew")
    paswword = ttk.Entry(window)
    paswword.grid(row=1, column=1, sticky="ew")
    
    ttk.Label(window, text="Password confirm:").grid(row=2, column=0,sticky="ew")
    paswword2 = ttk.Entry(window)
    paswword2.grid(row=2, column=1, sticky="ew")
    
    
    ttk.Button(window, text="Register",command=lambda:add_usser.add_user(usuario.get(),paswword.get(),paswword2.get(),window)).grid(row=3, column=1, pady=10)
    ttk.Button(window, text="Volver",command=lambda :volver.volver()).grid(row=3, column=0, pady=10)
    
    error = ttk.Label(window)
    error.grid(row=4, column=0,sticky="ew",columnspan=2)

    window.mainloop()
    
    return add_active
    