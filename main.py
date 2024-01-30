# from controlador.profesor_controlador import ProfesorControlador

# def menu():
#     controlador = ProfesorControlador()

#     while True:
#         print("\n1. Listar profesores")
#         print("2. Agregar profesor")
#         print("3. Actualizar profesor")
#         print("4. Eliminar profesor")
#         print("5. Salir")
#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             controlador.listar_profesores()
#         elif opcion == '2':
#             controlador.agregar_profesor()
#         elif opcion == '3':
#             controlador.actualizar_profesor()
#         elif opcion == '4':
#             controlador.eliminar_profesor()
#         elif opcion == '5':
#             break

# if __name__ == "__main__":
#     menu()



from controlador.profesor_controlador import ProfesorControlador
from vista.profesor_vista import ProfesorVista

def main():
    controlador = ProfesorControlador()
    vista = ProfesorVista(controlador)
    vista.mainloop()

if __name__ == "__main__":
    main()
