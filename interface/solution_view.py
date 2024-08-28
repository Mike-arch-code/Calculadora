from tkinter import TclError, ttk

def create_answer_frame(container):

    global label
    
    label = ttk.Label(container, font=("Arial", 18))

    return label