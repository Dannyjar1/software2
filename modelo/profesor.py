


from pymongo import MongoClient

class ProfesorModelo:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['universidad']
        self.collection = self.db['profesor']

    def obtener_profesores(self):
        return list(self.collection.find({}))

    def agregar_profesor(self, datos_profesor):
        self.collection.insert_one(datos_profesor)

    def eliminar_profesor(self, codigo):
        self.collection.delete_one({"codigo": codigo})

    def actualizar_profesor(self, codigo, datos_profesor):
        self.collection.update_one({"codigo": codigo}, {"$set": datos_profesor})

