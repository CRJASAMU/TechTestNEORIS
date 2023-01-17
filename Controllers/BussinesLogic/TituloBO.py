from Controllers.CRUD.TituloDAO import TituloDAO
from Entities.DTOTitulo import DTOTitulo
from pprint import pprint

class TituloBO:
    def __init__(self, titulo_dao: TituloDAO):
        self.titulo_dao = titulo_dao

    def titulos_registrados(self):
        titulos_registrados = len(self.titulo_dao.leer())
        print("El numero de titulos registrados son: {}".format(titulos_registrados))

    def validar_cuota(self, tabla_titulos: list[DTOTitulo]):
        if (len(tabla_titulos) == 0):
            print("La tabla no cuenta con registros que validar")
            return
        for titulo in tabla_titulos:
            if (titulo["pagocuota"] == "y"):
                print("El titulo {} fue pagado".format(titulo))
            else:
                print("El titulo {} no fue pagado".format(titulo))

    def validar_cuota_por_id_titulo(self, id_titulo: str):
        tabla_filtrada: list[DTOTitulo] = self.titulo_dao.leer_por_id_titulo(
            idtitulo=id_titulo)
        self.validar_cuota(tabla_titulos=tabla_filtrada)

    def actualizar_fecha_de_creacion(self, antigua_fecha_de_creacion: str, nueva_fecha_de_creacion: str):
        tabla_filtrada: list[DTOTitulo] = self.titulo_dao.leer_por_fecha_de_creacion(
            antigua_fecha_de_creacion)
        for titulo in tabla_filtrada:
            titulo["fecha_de_creacion"] = nueva_fecha_de_creacion
        self.titulo_dao.eliminar_por_fecha_de_creacion(
            fecha_de_creacion=antigua_fecha_de_creacion)
        nueva_tabla: list[DTOTitulo] = self.titulo_dao.leer()
        nueva_tabla.extend(tabla_filtrada)
        self.titulo_dao.actualizar(tabla_titulos_actualizada=nueva_tabla)

    def eliminar_por_id_titulo_solicitado(self, id_titulo: int):
        self.titulo_dao.eliminar_por_id_titulo(id_titulo=id_titulo)

    def imprimir_listado_titulos(self):
        tabla_titulos = self.titulo_dao.leer()
        if len(tabla_titulos) == 0:
            print("La tabla titulos no tiene información")
            return
        pprint("Los titulos creados son: \n {}".format(tabla_titulos),indent=3)
