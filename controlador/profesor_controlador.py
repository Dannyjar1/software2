


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

    


