from data_base import class_firebase_database
from interface import input_bar
from interface import historial_frame
from interface import login
from interface import history_offline

def save():
    name = login.name
    histioral = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
    position_database = "/Usuarios/"+str(name)+"/Historial/" + str(len(histioral))
    class_firebase_database.write_record(position_database, input_bar.text_bar.get())
    historial_frame.actulice_historial()
    
def save_offline():
    new_entry = input_bar.text_bar.get()
    historial_file_path = 'assets\\historial.txt'
    try:
        with open(historial_file_path, 'r') as file:
            historial_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        historial_list = []

    historial_list.append(new_entry)

    with open(historial_file_path, 'w') as file:
        for item in historial_list:
            file.write(f"{item}\n")
    history_offline.actulice_historial()
    
def save_offline_to_online(frame,op):
    
    if op:
        try:
            with open("assets\\historial.txt", 'r') as file:
                historial_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            historial_list = []

        if len(historial_list) > 0:
            name = login.name
            histioral = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
            for i, conten in enumerate(historial_list):
                position_database = "/Usuarios/"+str(name)+"/Historial/" + str(len(histioral)+i)
                class_firebase_database.write_record(position_database, conten)
            with open("assets\\historial.txt", 'w') as archivo:
                pass
            return frame.destroy()
    else:
        with open("assets\\historial.txt", 'w') as archivo:
             pass
        return frame.destroy()