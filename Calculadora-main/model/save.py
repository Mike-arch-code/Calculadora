from firebase_admin import  db
from data_base import class_firebase_database
from interface import input_bar
from interface import historial_frame
from model import size_window
from interface import login

def save():
    name = login.name
    histioral = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
    position_database = "/Usuarios/"+str(name)+"/Historial/" + str(len(histioral))
    class_firebase_database.write_record(position_database, input_bar.text_bar.get())
    if size_window.historial:
        historial_frame.actulice_historial()
    