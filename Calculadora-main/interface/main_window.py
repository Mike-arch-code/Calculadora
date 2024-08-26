import tkinter as tk
from tkinter import ttk
from interface import central_frame
def create_main_window(a):

    global window

    window = tk.Tk()
    window.title("Calculadora Grafica")
    window.minsize(300,500)
    window.geometry("300x500")
    window.config(bg='black')    

    window.columnconfigure(0,weight=0)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=0)
    
    window.rowconfigure(0, weight=2)

    center = central_frame.frame_central(window,a)
    center.grid(column=1,row=0,sticky="nsew")



    window.protocol("WM_DELETE_WINDOW", window.quit)
    

    return window

