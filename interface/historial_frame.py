from tkinter import TclError, ttk
from data_base import class_firebase_database
from model import clear_historial
from model import input_bar_fuctions
from interface import login
from interface import internet

conten_historial = False

def historial(container):
    name = login.name
    try:
        global conten_historial
        global window
        window = ttk.Frame(container,borderwidth=1,relief='solid')
        s = ttk.Style()
        s.configure('my.TButton', font=('Arial',12))
        window.columnconfigure(0,weight=1)
        window.columnconfigure(1,weight=1)
        
        if len(class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")) > 1:
            conten_historial = True
        if not conten_historial:
            ttk.Label(window,text="No hay historial").grid(column=0, row=0,sticky="nsew")
        else:

            num_historial = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
            num_historial = len(num_historial)


            for i in range (1,num_historial):

                conten = (class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/"+ str(i)))
                ttk.Button(window, style='my.TButton', compound="center",command=lambda conten = conten :input_bar_fuctions.historial(conten),text=(conten)).grid(column=0, row=(num_historial-i),sticky="nsew")
                ttk.Button(window, style='my.TButton', compound="center",command=lambda i = i :clear_historial.clear((i)),text=("Delete")).grid(column=1, row=(num_historial-i),sticky="nsew")

        return window
    except:
        internet.internet()
    
        

def actulice_historial():
    name = login.name
    
    try:
        global conten_historial
        conten_historial = True

        window.columnconfigure(0,weight=1)
        window.columnconfigure(1,weight=1)
        for widget in window.winfo_children():
            widget.destroy()

        num_historial = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
        num_historial = len(num_historial)

        for i in range (1,num_historial):

            conten = (class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/"+ str(i)))
            ttk.Button(window, style='my.TButton', compound="center",command=lambda conten = conten :input_bar_fuctions.historial(conten),text=(conten)).grid(column=0, row=(num_historial-i),sticky="nsew")
            ttk.Button(window, style='my.TButton', compound="center",command=lambda i = i :clear_historial.clear((i)),text=("Delete")).grid(column=1, row=(num_historial-i),sticky="nsew")
    except:
        internet.internet()
