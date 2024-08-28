import tkinter as tk
from interface import central_frame
from tkinter import TclError, ttk
from model import volver
from interface import grafic_frame
from interface import historial_frame
from interface import history_offline
from control import controller
def create_main_window():

    global window
    global letf
    global right

    window = tk.Tk()
    if controller.offoline:
        window.title("Calculadora Grafica offline")
    else:
        window.title("Calculadora Grafica online")
    window.minsize(300,500)
    window.geometry("300x500")

    window.columnconfigure(0,weight=0)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=0)
    
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=13)
    
    ttk.Button(window, text="Volver",command=lambda :volver.volver()).grid(row=0, column=1,sticky="nsew")


    center = central_frame.frame_central(window)
    center.grid(column=1,row=1,sticky="nsew")
    
    letf = grafic_frame.grafic(window)
    
    if controller.offoline:
        right = history_offline.historial(window)
    else:
        right = historial_frame.historial(window)



    window.protocol("WM_DELETE_WINDOW", window.quit)
    

    window.mainloop()

