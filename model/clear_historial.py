from data_base import class_firebase_database
from interface import historial_frame
from interface import login
from interface import history_offline

def clear(x):
    name = login.name
    historial = class_firebase_database.read_record("/Usuarios/"+str(name)+"/Historial/")
    del historial[x]
    value_historial = len(historial)
    for i in range(value_historial):
        class_firebase_database.write_record("/Usuarios/"+str(name)+"/Historial/"+str(i),historial[i])

    class_firebase_database.delete_record("/Usuarios/"+str(name)+"/Historial/"+str(value_historial))
    historial_frame.actulice_historial()
    
def clear_historial_item(index, historial_list):
    """Elimina un elemento del historial basado en su índice y actualiza el archivo de texto."""
    if 0 <= index - 1 < len(historial_list):
        historial_file_path = 'assets\\historial.txt'
        del historial_list[index - 1]
        with open(historial_file_path, 'w') as file:
            for item in historial_list:
                file.write(f"{item}\n")
        history_offline.actulice_historial()
