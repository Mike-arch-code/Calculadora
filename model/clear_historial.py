from data_base import class_firebase_database
from interface import historial_frame
from interface import login

def clear(x):
    name = login.name
    historial = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
    del historial[x]
    value_historial = len(historial)
    for i in range(value_historial):
        class_firebase_database.write_record("/Usuarios/"+str(name)+"/Historial/"+str(i),historial[i])

    class_firebase_database.delete_record("/Usuarios/"+str(name)+"/Historial/"+str(value_historial))
    historial_frame.actulice_historial()
