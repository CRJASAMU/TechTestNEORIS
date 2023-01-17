import unittest
from Connection import BaseDeDatos
from Entities import DTODataBase, DTOTitulo
from Controllers.CRUD import TituloDAO
from Tools import ObtenerConfiguraciones
import random


class TestTituloDAO(unittest.TestCase):

    def setUp(self):
        self.connection_string = ObtenerConfiguraciones()[
            "DataBase"]["test_connection_string"]
        self.base_de_datos = BaseDeDatos(self.connection_string)
        self.titulo_dao = TituloDAO(self.base_de_datos)

    def test_leer(self):
        result = self.titulo_dao.leer()
        self.assertIsInstance(result, list)
        self.assertEqual(result[-1], {'id': 3, 'idtitulo': 3, 'titulo': 2, 'clasificacion': '', 'valor': 360000000,
                         'fecha_de_creacion': '2022-02-16', 'fecha_de_vencimiento': '2023-02-17', 'pagocuota': 'y'})

    def test_leer_por_id_titulo(self):
        result = self.titulo_dao.leer_por_id_titulo(1)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['idtitulo'], 1)

    def test_actualizar(self):
        valor_aleatorio = random.randint(10000, 100000)
        tabla_titulos = self.titulo_dao.leer()
        tabla_titulos[0]['valor'] = valor_aleatorio
        self.titulo_dao.actualizar(tabla_titulos)
        tabla_titulos_actualizada = self.titulo_dao.leer()
        self.assertEqual(
            tabla_titulos_actualizada[0]['valor'], valor_aleatorio)


if __name__ == '__main__':
    unittest.main()
