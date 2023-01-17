
from Connection import BaseDeDatos
from Entities import DTODataBase, DTOTitulo
from jsonschema import validate


class TituloDAO:

    def __init__(self, instancia_base_de_datos: BaseDeDatos):
        self.instancia_base_de_datos = instancia_base_de_datos

    # Funciones leer

    def leer(self):
        base_de_datos: DTODataBase = self.instancia_base_de_datos.obtener()
        return base_de_datos["titulos"]

    def leer_por_id_titulo(self, idtitulo: int)->list[DTOTitulo]:
        tabla_titulos: list[DTOTitulo] = self.leer()
        tabla_filtrada: list[DTOTitulo] = list(
            filter(lambda titulos: titulos["idtitulo"] == idtitulo, tabla_titulos))
        return tabla_filtrada

    def leer_por_fecha_de_creacion(self, fecha_de_creacion: str):
        tabla_titulos: list[DTOTitulo] = self.leer()
        tabla_filtrada: list[DTOTitulo] = list(
            filter(lambda titulos: titulos["fecha_de_creacion"] == fecha_de_creacion, tabla_titulos))
        return tabla_filtrada
    # Funciones Actualizar

    def actualizar(self, tabla_titulos_actualizada: list[DTOTitulo]):
        base_de_datos: DTODataBase = self.instancia_base_de_datos.obtener()
        base_de_datos["titulos"] = tabla_titulos_actualizada
        self.instancia_base_de_datos.actualizar(base_de_datos)

    def actualizar_por_id(self, id: int, nuevo_titulo: DTOTitulo):
        tabla_titulos: list[DTOTitulo] = self.leer()
        for index, titulo in enumerate(tabla_titulos):
            if titulo["id"] == id:
                tabla_titulos[index] = nuevo_titulo
                break
        self.actualizar(
            tabla_titulos_actualizada=tabla_titulos)

    # Funciones Crear
    def crear(self, titulo: DTOTitulo):
        tabla_titulos = self.leer()
        tabla_titulos.append(titulo)
        self.actualizar(
            tabla_titulos_actualizada=tabla_titulos)

    # Funciones Eliminar
    def eliminar_por_id(self, id: int):
        tabla_titulos: list[DTOTitulo] = self.leer()
        tabla_filtrada: list[DTOTitulo] = list(
            filter(lambda titulos: titulos["id"] != id, tabla_titulos))
        self.actualizar(
            tabla_titulos_actualizada=tabla_filtrada)

    def eliminar_por_id_titulo(self, id_titulo: int):
        tabla_titulos: list[DTOTitulo] = self.leer()
        tabla_filtrada: list[DTOTitulo] = list(
            filter(lambda titulos: titulos["idtitulo"] != id_titulo, tabla_titulos))
        self.actualizar(
            tabla_titulos_actualizada=tabla_filtrada)

    def eliminar_por_fecha_de_creacion(self, fecha_de_creacion: str):
        tabla_titulos: list[DTOTitulo] = self.leer()
        tabla_filtrada: list[DTOTitulo] = list(
            filter(lambda titulos: titulos["fecha_de_creacion"] != fecha_de_creacion, tabla_titulos))
        self.actualizar(
            tabla_titulos_actualizada=tabla_filtrada)
