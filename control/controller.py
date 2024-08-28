from interface import main_window
from data_base import class_firebase_database
from interface import window_log
from interface import login
from interface import register

base_active = False

def controller_aplication():
    global offoline
    offoline = False
    
    global base_active
    
    opcion = window_log.log()

    if opcion == 1:
        class_firebase_database.init()
        offoline = False
        autentication = login.login()
        if autentication:
            main_window.create_main_window()
    elif opcion == 2:
        class_firebase_database.init()
        base_active = True
        offoline = False
        registro = True
        if registro:
            value = register.register()
            if value:
                autentication = login.login()
                if autentication:
                    main_window.create_main_window()
            
    elif opcion == 3:
        offoline = True
        main_window.create_main_window()
    
    
    
    

