from interface import main_window
from interface import grafic_frame
from model import operaciones
import numpy as np

grafic = False
historial = False

def grafic_size():
    global grafic_entry
    global grafic
    global historial
    vacio = False
    if not grafic:
        grafic = True
        if not historial:
            main_window.window.columnconfigure(0,weight=7)
            main_window.letf.grid(column=0,row=0,sticky="nsew",rowspan=2)
            main_window.window.minsize(900,500)
            if not operaciones.vacio:
                y =[0]* 200
                Z = np.zeros_like(y)
                grafic_frame.actualice_grafic(y,y,Z)
        else:
            main_window.window.columnconfigure(0,weight=4)
            main_window.letf.grid(column=0,row=0,sticky="nsew",rowspan=2)
            main_window.window.minsize(1250,500)
            if not operaciones.vacio:
                y =[None]* 100
                Z = np.zeros_like(y)
                grafic_frame.actualice_grafic(y,y,Z)
    else:
        grafic = False
        if not historial:
            main_window.window.columnconfigure(0,weight=0)
            main_window.window.minsize(300,500)
            main_window.letf.grid_remove()
        else:
            main_window.window.columnconfigure(0,weight=0)
            main_window.window.minsize(600,500)
            main_window.letf.grid_remove()

def hitorial_size():
    global historial
    global grafic
    if not historial:
        historial = True
        if not grafic:
            main_window.window.columnconfigure(2,weight=1)
            main_window.right.grid(column=2,row=0,sticky="nsew",rowspan=2)
            main_window.window.minsize(600,500)
        else:
            main_window.window.columnconfigure(2,weight=1)
            main_window.right.grid(column=2,row=0,sticky="nsew",rowspan=2)
            main_window.window.minsize(1250,500)
    else:
        historial = False
        if not grafic:
            main_window.window.columnconfigure(2,weight=0)
            main_window.window.minsize(300,500)
            main_window.right.grid_remove()
        else:
            main_window.window.columnconfigure(2,weight=0)
            main_window.window.minsize(900,500)
            main_window.right.grid_remove()
    