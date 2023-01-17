
from Controllers.CRUD import TituloDAO
from Tools import ObtenerConfiguraciones
from Connection import BaseDeDatos
from Controllers.CRUD import TituloDAO
from Controllers.BussinesLogic import TituloBO

class MenuTitulos:
    def __init__(self):
        self.opciones = []
    
    def add_option(self, opcion):
        self.opciones.append(opcion)
    
    def run(self):
        while True:
            for i, opcion in enumerate(self.opciones):
                print(f"{i+1}. {opcion.name}")
            print("Presione q para Salir")
            seleccion = input("Seleccione una opción: ")
            if seleccion == "q":
                break
            else:
                try:
                    seleccion = int(seleccion)
                    self.opciones[seleccion-1].run()
                except (ValueError, IndexError):
                    print("Opción inválida.")

class Opcion:
    def __init__(self, name):
        self.name = name

    def run(self):
        pass

class OpcionA(Opcion):
    def __init__(self):
        super().__init__("Listar Titulos")
    
    def run(self):
        #TituloBO.imprimir_listado_titulos()
        print("Ejecutando opción A...")

class OpcionB(Opcion):
    def __init__(self):
        super().__init__("Registrar Titulo")
    
    def run(self):
        print("Ejecutando opción B...")

class OpcionC(Opcion):
    def __init__(self):
        super().__init__("Eliminar Titulo")
    
    def run(self):
        print("Ejecutando opción C...")



def Init ():
    menu = MenuTitulos()
    menu.add_option(OpcionA())
    menu.add_option(OpcionB())
    menu.add_option(OpcionC())
    menu.run()
    
if __name__ == '__main__':
    MenuTitulos.main()
