from tkinter import TclError, ttk
from interface import input_bar
from model import input_bar_fuctions
from control import controller

def create_button(x,y,name_button,logic):

    style = ttk.Style()
    style.configure("Bold.TButton", font=("Segoe UI", 12,"bold"))


    b = ttk.Button(logic, style="Bold.TButton",compound="center",command=lambda:input_bar_fuctions.write(input_bar.text_bar,name_button),text=(name_button)).grid(column=x, row=y,sticky="nsew")

def create_button_DELL(x,y,name_button,logic):
    s = ttk.Style()
    s.configure('my.TButton', font=('Helvetica',12))


    ttk.Button(logic, style='my.TButton', compound="center",text=(name_button),command=lambda:input_bar_fuctions.DEL(input_bar.text_bar)).grid(column=x, row=y,sticky="nsew",columnspan=2)

def create_button_ANS(x,y,name_button,logic):
    s = ttk.Style()
    s.configure('my.TButton', font=('Helvetica',12 ))


    ttk.Button(logic, style='my.TButton',compound="center",text=(name_button),command=lambda:input_bar_fuctions.ENTER(controller.offoline)).grid(column=x, row=y,sticky="nsew",columnspan=2)

    