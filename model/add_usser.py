from data_base import class_firebase_database
from interface import register


def add_user(username,password,password2,window):
    add = True
    
    try:
        usuarios = class_firebase_database.read_record("")
        usuarios = usuarios['Usuarios']
        matrix = [['Nombre', 'Clave', 'Historial']]
        if username != "" and password !="":
            for user, details in usuarios.items():
                matrix.append([user, details['Clave'], details['Historial']])
            
            for row in matrix:
                if row[0] == username:
                    return register.error.config(text="El nombre de usuario ya esta en uso")
                else:
                    add = True
                    
            if password == password2:
                if add == True:
                    class_firebase_database.write_record("/Usuarios/"+ username + "/Clave/",password)
                    class_firebase_database.write_record("/Usuarios/"+ username +"/Historial/0/", "Nuevo usuario" )
                    window.destroy()
                    register.add_active = True
            else:
                return register.error.config(text="Las contraseñas no coinciden")
        else:
            return register.error.config(text="Hay campos vacios")
    except:
        register.error.config(text="No se pudo conectar a la base de datos.\nRevise su conexión a Internet o acceda desde el modo offline.")

    