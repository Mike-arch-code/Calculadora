import firebase_admin
from firebase_admin import credentials, db

def init():
    cred = credentials.Certificate("key\\credenciales.json")
    firebase_admin.initialize_app(cred, {'databaseURL': "https://p-1-8c9a0-default-rtdb.firebaseio.com/"})

def write_record(path, data):
    ref = db.reference(path)
    ref.set(data)

def read_record(path):
    ref = db.reference(path)
    return ref.get()

def update_record(path, data):
    ref = db.reference(path)
    ref.update(data)

def delete_record(path):
    ref = db.reference(path)
    ref.delete()




    
                
