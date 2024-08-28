import tkinter as tk
from interface import expand_buttons
from tkinter import TclError, ttk
from interface import input_bar
from interface import keyboard
from interface import solution_view

def frame_central(container):

    window = ttk.Frame(container,borderwidth=1,relief='solid')

    window.columnconfigure(0,weight=2)
    window.rowconfigure(0,weight=1)
    window.rowconfigure(1,weight=2)
    window.rowconfigure(2,weight=1)
    window.rowconfigure(3,weight=5)

    expant = expand_buttons.expand_buttons(window)
    expant.grid(column=0,row=0,sticky="nsew")

    tex_bar = input_bar.input_bar(window)
    tex_bar.grid(column=0,row=1,sticky="nsew")

    solution = solution_view.create_answer_frame(window)
    solution.grid(column=0,row=2,sticky="nsew")

    teclado = keyboard.create_keyboard_frame(window)
    teclado.grid(column=0,row=3,sticky="nsew")


    return window