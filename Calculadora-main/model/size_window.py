import tkinter as tk
from tkinter import TclError, ttk
from interface import main_window
from interface import historial_frame
from interface import grafic_frame
from model import operaciones
import numpy as np

grafic = False
historial = False

def grafic_size():

    global grafic
    global historial
    if not grafic:
        grafic = True
        if not historial:
            main_window.window.columnconfigure(0,weight=7)
            main_window.left = grafic_frame.grafic(main_window.window)
            main_window.left.grid(column=0,row=0,sticky="nsew")
            main_window.window.minsize(900,500)
            if operaciones.vacio:
                grafic_frame.actualice_grafic(operaciones.y_values,operaciones.x_values,operaciones.Z)
            else:
                y =[0]* 200
                Z = np.zeros_like(y)
                grafic_frame.actualice_grafic(y,y,Z)
        else:
            main_window.window.columnconfigure(0,weight=4)
            main_window.left =  grafic_frame.grafic(main_window.window)
            main_window.left.grid(column=0,row=0,sticky="nsew")
            main_window.window.minsize(900,500)
            main_window.window.minsize(1250,500)
            if operaciones.vacio:
                grafic_frame.actualice_grafic(operaciones.y_values,operaciones.x_values,operaciones.Z)
                
            else:
                
                y =[None]* 100
                Z = np.zeros_like(y)
                grafic_frame.actualice_grafic(y,y,Z)

    else:
        grafic = False
        if not historial:
            main_window.window.columnconfigure(0,weight=0)
            main_window.window.minsize(300,500)
            main_window.left.grid_remove()
        else:
            main_window.window.columnconfigure(0,weight=0)
            main_window.window.minsize(600,500)
            main_window.left.grid_remove()

def hitorial_size():
    global historial
    global grafic
    if not historial:
        historial = True
        if not grafic:
            main_window.window.columnconfigure(2,weight=1)
            main_window.central1 = historial_frame.historial(main_window.window)
            main_window.central1.grid(column=2,row=0,sticky="nsew")
            main_window.window.minsize(600,500)
        else:
            main_window.window.columnconfigure(2,weight=1)
            main_window.central1 = historial_frame.historial(main_window.window)
            main_window.central1.grid(column=2,row=0,sticky="nsew")
            main_window.window.minsize(1250,500)
    else:
        historial = False
        if not grafic:
            main_window.window.columnconfigure(2,weight=0)
            main_window.window.minsize(300,500)
            main_window.central1.grid_remove()
        else:
            main_window.window.columnconfigure(2,weight=0)
            main_window.window.minsize(900,500)
            main_window.central1.grid_remove()
    