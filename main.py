

from controlador.profesor_controlador import ProfesorControlador
from vista.profesor_vista import ProfesorVista

def main():
    controlador = ProfesorControlador()
    vista = ProfesorVista(controlador)
    vista.mainloop()

if __name__ == "__main__":
    main()
