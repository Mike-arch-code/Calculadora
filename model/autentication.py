from firebase_admin import  db
from data_base import class_firebase_database
from interface import login
from interface import history_offline

value =  False

def autentication(username,password,window):
    global value
    
    try:
        usuarios = class_firebase_database.read_record("")
        usuarios = usuarios['Usuarios']
        matrix = [['Nombre', 'Clave', 'Historial']]
        for user, details in usuarios.items():
            matrix.append([user, details['Clave'], details['Historial']])
        for row in matrix:
            if row[0] == username:
                if str(row[1]) == password:   
                    window.destroy()
                    login.name = username
                    value = True
                    with open("assets\\historial.txt", 'r') as archivo:
                        contenido = archivo.read()
                        if contenido:
                            value == False
                            history_offline.subir_historial()
                        else:
                            return value   
        if value == False:
            login.error.config(text="Los datos no coninciden")
    except:
        login.error.config(text="No se pudo conectar a la base de datos.\nRevise su conexión a Internet o acceda desde el modo offline.")
                   


    