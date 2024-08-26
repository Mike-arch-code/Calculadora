from data_base import class_firebase_database


def delete_historial ():
    historial  = class_firebase_database.read_record("/Historial/")
    historial = len(historial)
    for i in range(1,historial):
        class_firebase_database.delete_record("/Historial/"+str(i))