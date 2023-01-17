import unittest
from Connection import BaseDeDatos
from unittest.mock import patch
from Controllers.CRUD import TituloDAO
from Controllers.BussinesLogic import TituloBO
from Tools import ObtenerConfiguraciones


class TestTituloBO(unittest.TestCase):
    def setUp(self):
        self.connection_string = ObtenerConfiguraciones()[
            "DataBase"]["test_connection_string"]
        self.base_de_datos = BaseDeDatos(self.connection_string)
        self.titulo_dao = TituloDAO(self.base_de_datos)
        self.titulo_logica_de_negocio = TituloBO(titulo_dao=self.titulo_dao)

    @patch('builtins.print')
    def test_titulos_registrados(self, mock_print):
        self.titulo_logica_de_negocio.titulos_registrados()
        mock_print.assert_called_with(
            'El numero de titulos registrados son: 3')

    @patch('builtins.print')
    def test_validar_cuota_sin_datos(self, mock_print):
        self.titulo_logica_de_negocio.validar_cuota([])
        mock_print.assert_called_with(
            'La tabla no cuenta con registros que validar')

    @patch('builtins.print')
    def test_validar_cuota(self, mock_print):
        self.titulo_logica_de_negocio.validar_cuota(self.titulo_dao.leer())
        mock_print.assert_called_with(
            "El titulo {'id': 3, 'idtitulo': 3, 'titulo': 2, 'clasificacion': '', 'valor': 360000000, 'fecha_de_creacion': '2022-02-21', 'fecha_de_vencimiento': '2023-02-17', 'pagocuota': 'y'} fue pagado")

    def test_actualizar_fecha_de_creacion(self):
        antigua_fecha_de_creacion = "2022-02-16"
        nueva_fecha_de_creacion = "2022-02-21"
        self.titulo_logica_de_negocio.actualizar_fecha_de_creacion(
            antigua_fecha_de_creacion=antigua_fecha_de_creacion,
            nueva_fecha_de_creacion=nueva_fecha_de_creacion)
        tabla_actualizada = self.titulo_dao.leer()
        self.assertEqual(tabla_actualizada[-1], {'id': 3, 'idtitulo': 3, 'titulo': 2, 'clasificacion': '',
                         'valor': 360000000, 'fecha_de_creacion': '2022-02-21', 'fecha_de_vencimiento': '2023-02-17', 'pagocuota': 'y'})


if __name__ == '__main__':
    unittest.main()
