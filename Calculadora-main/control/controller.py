from interface import main_window
from data_base import class_firebase_database
from interface import window_log
from interface import login
from interface import register


def controller_aplication():
    global offoline
    offoline = False
    
    opcion = window_log.log()
    
    if opcion == 1:
        class_firebase_database.init()
        offoline = False
        autentication = login.login()
        if autentication:
            window = main_window.create_main_window(offoline)
            window.mainloop()
    elif opcion == 2:
        class_firebase_database.init()
        offoline = False
        registro = True
        if registro:
            value = register.register()
            if value:
                autentication = login.login()
                if autentication:
                    window = main_window.create_main_window(offoline)
                    window.mainloop()
            
    elif opcion == 3:
        offoline = True
        window = main_window.create_main_window(offoline)
        window.mainloop()
    
    
    
    

