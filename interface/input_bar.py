
from tkinter import TclError, ttk

def input_bar(container):

    global text_bar

    frame = ttk.Frame(container)

    frame.columnconfigure(0,weight=1)
    frame.rowconfigure(0,weight=1)

    hotizontal_scrollbar = ttk.Scrollbar(frame, orient ="horizontal")
    font_size = ("Arial",22)
    text_bar = ttk.Entry(frame,font=font_size, xscrollcommand=hotizontal_scrollbar.set)
    text_bar.grid(column=0,row=0,sticky="nsew")
    hotizontal_scrollbar.config(command=text_bar.xview)
    hotizontal_scrollbar.grid(column=0,row=1,sticky="ew")
    text_bar.focus_set()
    return frame