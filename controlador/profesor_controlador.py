# from modelo.profesor import ProfesorModelo
# from vista.profesor_vista import ProfesorVista

# class ProfesorControlador:
#     def __init__(self):
#         self.modelo = ProfesorModelo()
#         self.vista = ProfesorVista()

#     def listar_profesores(self):
#         profesores = self.modelo.obtener_profesores()
#         self.vista.mostrar_profesores(profesores)

#     def agregar_profesor(self):
#         datos_profesor = self.vista.obtener_datos_profesor()
#         self.modelo.agregar_profesor(*datos_profesor)
#         self.vista.mostrar_mensaje("Profesor agregado correctamente.")

#     def actualizar_profesor(self):
#         datos_profesor = self.vista.obtener_datos_profesor()
#         self.modelo.actualizar_profesor(*datos_profesor)
#         self.vista.mostrar_mensaje("Profesor actualizado correctamente.")

#     def eliminar_profesor(self):
#         codigo = input("Ingrese el código del profesor a eliminar: ")
#         self.modelo.eliminar_profesor(codigo)
#         self.vista.mostrar_mensaje("Profesor eliminado correctamente.")




# from modelo.profesor import ProfesorModelo


# class ProfesorControlador:
#     def __init__(self):
#         self.modelo = ProfesorModelo()

#     def obtener_profesores(self):
#         try:
#             profesores = self.modelo.obtener_profesores()
#             return profesores
#         except Exception as e:
#             print(f"An error occurred while obtaining professors: {e}")
#             # Handle the exception as needed, e.g., log to a file, or return an empty list
#             return []
        

#     def agregar_profesor(self, codigo, nombre, carrera, especialidad, ingreso):
#         profesor = {
#             "codigo": codigo, 
#             "nombre": nombre,
#             "carrera": carrera,
#             "especialidad": especialidad,
#             "ingreso": ingreso
#         }
#         self.modelo.agregar_profesor(profesor)

#     def actualizar_profesor(self, codigo, nombre, carrera, especialidad, ingreso):
#         profesor = {
#             "codigo": codigo, 
#             "nombre": nombre,
#             "carrera": carrera,
#             "especialidad": especialidad,
#             "ingreso": ingreso
#         }
#         self.modelo.actualizar_profesor(codigo, profesor)

#     def eliminar_profesor(self, codigo):
#         self.modelo.eliminar_profesor(codigo)

#     # Additional method to search for a professor by name, career, specialty, or entry year.
#     def buscar_profesores(self, filtro):
#         return self.modelo.buscar_profesores(filtro)





from modelo.profesor import ProfesorModelo

class ProfesorControlador:
    def __init__(self):
        self.modelo = ProfesorModelo()

    def obtener_profesores(self):
        return self.modelo.obtener_profesores()

    def agregar_profesor(self, codigo, nombre, carrera,especialidad, ingreso):
        profesor = {"codigo": codigo, "nombre": nombre, "carrera":carrera, "especialidad":especialidad,"ingreso":ingreso  }
        self.modelo.agregar_profesor(profesor)

    def eliminar_profesor(self, codigo):
        self.modelo.eliminar_profesor(codigo)

    def actualizar_profesor(self, codigo, nombre, carrera, especialidad, ingreso):
     profesor = {
        "codigo": codigo,
        "nombre": nombre,
        "carrera": carrera,
        "especialidad": especialidad,
        "ingreso": ingreso
    }
     self.modelo.actualizar_profesor(codigo, profesor)

    


