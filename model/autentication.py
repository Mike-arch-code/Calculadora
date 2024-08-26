from firebase_admin import  db
from data_base import class_firebase_database
from interface import login

value =  False

def autentication(username,password,window):
    global value
    
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
                return value
    return value
                   


    