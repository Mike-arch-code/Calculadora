import tkinter as tk
from interface import input_bar
from tkinter import TclError
from model import operaciones
from model import save
from interface import historial_frame

def write(text_bar,character):

    current_position = text_bar.index(tk.INSERT)
    text_bar.insert(current_position,character)
    text_bar.focus_set()

def DEL(text_bar):
    current_position = text_bar.index(tk.INSERT)
    if current_position > 0:
        text_bar.delete(current_position - 1)
    text_bar.focus_set()


def ENTER(a):
    if not a:
        save.save()
    historial_frame.conten_historial = True
    operaciones.operaction()

def historial(contenido):
    input_bar.text_bar.delete(0, tk.END)
    input_bar.text_bar.insert(0,contenido)

    
