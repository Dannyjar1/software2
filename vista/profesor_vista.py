# class ProfesorVista:
#     def mostrar_profesores(self, profesores):
#         for profesor in profesores:
#             print(f"Código: {profesor['codigo']}, Nombre: {profesor['nombre']}, Carrera: {profesor['carrera']}, Especialidad: {profesor['especialidad']}, Ingreso: {profesor['ingreso']}")

#     def obtener_datos_profesor(self):
#         codigo = input("Ingrese el código: ")
#         nombre = input("Ingrese el nombre: ")
#         carrera = input("Ingrese la carrera: ")
#         especialidad = input("Ingrese la especialidad: ")
#         ingreso = input("Ingrese la fecha de ingreso: ")
#         return (codigo, nombre, carrera, especialidad, ingreso)

#     def mostrar_mensaje(self, mensaje):
#         print(mensaje)




import tkinter as tk
from tkinter import ttk, messagebox

class ProfesorVista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Profesores")
        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.ventana)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Código:").grid(row=0, column=0, sticky="w")
        self.codigo = tk.Entry(self.frame)
        self.codigo.grid(row=0, column=1)

        tk.Label(self.frame, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.nombre = tk.Entry(self.frame)
        self.nombre.grid(row=1, column=1)


        tk.Label(self.frame, text="Carrera:").grid(row=2, column=0, sticky="w")
        self.carrera = tk.Entry(self.frame)
        self.carrera.grid(row=2, column=1)

        tk.Label(self.frame, text="Especialidad:").grid(row=3, column=0, sticky="w")
        self.especialidad = tk.Entry(self.frame)
        self.especialidad.grid(row=3, column=1)

        tk.Label(self.frame, text="Ingreso:").grid(row=4, column=0, sticky="w")
        self.ingreso = tk.Entry(self.frame)
        self.ingreso.grid(row=4, column=1)

        # tk.Button(self.frame, text="Agregar", command=self.agregar_profesor).grid(row=2, column=0, columnspan=2, pady=5)
        # tk.Button(self.frame, text="Eliminar", command=self.eliminar_profesor).grid(row=3, column=0, columnspan=2, pady=5)
        # tk.Button(self.frame, text="Actualizar", command=self.actualizar_profesor).grid(row=5, column=0, columnspan=2, pady=5)

        # self.tabla = ttk.Treeview(self.frame, columns=("codigo", "nombre", "carrera", "especialidad", "ingreso"), show='headings')
        # self.tabla.heading("codigo", text="Código")
        # self.tabla.heading("nombre", text="Nombre")
        # self.tabla.heading("carrera", text="Carrera")
        # self.tabla.heading("especialidad", text="Especialidad")
        # self.tabla.heading("ingreso", text="Ingreso")

        self.btn_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_profesor)
        self.btn_agregar.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        self.btn_eliminar = tk.Button(self.frame, text="Eliminar", command=self.eliminar_profesor)
        self.btn_eliminar.grid(row=6, column=0, columnspan=2, pady=(5, 0))

        self.btn_actualizar = tk.Button(self.frame, text="Actualizar", command=self.actualizar_profesor)
        self.btn_actualizar.grid(row=7, column=0, columnspan=2, pady=(5, 0))

    # Configuración de la tabla
        self.tabla = ttk.Treeview(self.frame, columns=("codigo", "nombre", "carrera", "especialidad", "ingreso"), show='headings')
        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("carrera", text="Carrera")
        self.tabla.heading("especialidad", text="Especialidad")
        self.tabla.heading("ingreso", text="Ingreso")
        self.tabla.grid(row=8, column=0, columnspan=2, pady=(10, 0))



    def agregar_profesor(self):
        codigo = self.codigo.get()
        nombre = self.nombre.get()
        carrera = self.carrera.get()
        especialidad = self.especialidad.get()
        ingreso  = self.ingreso.get()
        
        if codigo and nombre:
            self.controlador.agregar_profesor(codigo, nombre, carrera, especialidad, ingreso)
            self.limpiar_campos()  # Assuming you want to clear the fields after adding
            self.actualizar_tabla()

    def eliminar_profesor(self):
        seleccionado = self.tabla.focus()
        if seleccionado:
            datos = self.tabla.item(seleccionado)
            self.controlador.eliminar_profesor(datos['values'][0])
            self.actualizar_tabla()


    def obtener_datos_profesor(self):
        return {
            "codigo": self.codigo.get(),
            "nombre": self.nombre.get(),
            "carrera": self.carrera.get(),
            "especialidad": self.especialidad.get(),
            "ingreso": self.ingreso.get()
        }
    

    def actualizar_profesor(self):
      datos_profesor = self.obtener_datos_profesor()
      if datos_profesor["codigo"]:
        self.controlador.actualizar_profesor(**datos_profesor)  # Use argument unpacking
        self.limpiar_campos()
        self.actualizar_tabla()


    


    def limpiar_campos(self):
        self.codigo.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.carrera.delete(0, tk.END)
        self.especialidad.delete(0, tk.END)
        self.ingreso.delete(0, tk.END)


    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        profesores = self.controlador.obtener_profesores()
        for profesor in profesores:
            self.tabla.insert('', 'end', values=(profesor['codigo'], profesor['nombre']))

    def mainloop(self):
        self.actualizar_tabla()
        self.ventana.mainloop()

    # def setup_ui(self):
    # # ... Configuración de los widgets de entrada ...

    # # Configuración de los botones
    #  self.btn_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_profesor)
    #  self.btn_agregar.grid(row=5, column=0, columnspan=2, pady=(10, 0))

    #  self.btn_eliminar = tk.Button(self.frame, text="Eliminar", command=self.eliminar_profesor)
    #  self.btn_eliminar.grid(row=6, column=0, columnspan=2, pady=(5, 0))

    #  self.btn_actualizar = tk.Button(self.frame, text="Actualizar", command=self.actualizar_profesor)
    #  self.btn_actualizar.grid(row=7, column=0, columnspan=2, pady=(5, 0))

    # # Configuración de la tabla
    #  self.tabla = ttk.Treeview(self.frame, columns=("codigo", "nombre", "carrera", "especialidad", "ingreso"), show='headings')
    #  self.tabla.heading("codigo", text="Código")
    #  self.tabla.heading("nombre", text="Nombre")
    #  self.tabla.heading("carrera", text="Carrera")
    #  self.tabla.heading("especialidad", text="Especialidad")
    #  self.tabla.heading("ingreso", text="Ingreso")
    #  self.tabla.grid(row=8, column=0, columnspan=2, pady=(10, 0))

