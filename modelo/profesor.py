# from pymongo import MongoClient

# class ProfesorModelo:
#     def __init__(self):
#         self.client = MongoClient('mongodb://localhost:27017/')
#         self.db = self.client['universidad']
#         self.collection = self.db['profesor']

#     def obtener_profesores(self):
#         return list(self.collection.find({}))

#     def agregar_profesor(self, codigo, nombre, carrera, especialidad, ingreso):
#         profesor = {
#             "codigo": codigo,
#             "nombre": nombre,
#             "carrera": carrera,
#             "especialidad": especialidad,
#             "ingreso": ingreso
#         }
#         self.collection.insert_one(profesor)

#     def actualizar_profesor(self, codigo, nombre, carrera, especialidad, ingreso):
#         query = {"codigo": codigo}
#         new_values = {"$set": {
#             "nombre": nombre,
#             "carrera": carrera,
#             "especialidad": especialidad,
#             "ingreso": ingreso
#         }}
#         self.collection.update_one(query, new_values)

#     def eliminar_profesor(self, codigo):
#         query = {"codigo": codigo}
#         self.collection.delete_one(query)



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

