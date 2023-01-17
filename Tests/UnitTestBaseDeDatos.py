import unittest
import json
from Tools import ObtenerConfiguraciones
from Connection import BaseDeDatos


class TestBaseDeDatos(unittest.TestCase):
    def setUp(self):
        self.connection_string = ObtenerConfiguraciones()[
            "DataBase"]["test_connection_string"]
        self.data = {
            "id_titulos": [
                {
                    "id": 1,
                    "name": "USD"
                },
                {
                    "id": 2,
                    "name": "TRPV"
                },
                {
                    "id": 3,
                    "name": "TP"
                },
                {
                    "id": 4,
                    "name": "TID"
                },
                {
                    "id": 5,
                    "name": "THI"
                },
                {
                    "id": 6,
                    "name": "TESU"
                },
                {
                    "id": 7,
                    "name": "TEST"
                },
                {
                    "id": 8,
                    "name": "TESP"
                },
                {
                    "id": 9,
                    "name": "TESOROS"
                },
                {
                    "id": 10,
                    "name": "TESI"
                }
            ],
            "titulos_preestablecidos": [
                {
                    "id": 1,
                    "valor": "DOLAR"
                },
                {
                    "id": 2,
                    "valor": "TITULO DE PARTICIPACION RENTA VARIABLE"
                },
                {
                    "id": 3,
                    "valor": "TITULO DE PARTICIPACION"
                },
                {
                    "id": 4,
                    "valor": "TITULOS HIPOTECARIOS"
                },
                {
                    "id": 5,
                    "valor": "TES UVR"
                },
                {
                    "id": 6,
                    "valor": "TES TRM"
                },
                {
                    "id": 7,
                    "valor": "TES PESOS"
                },
                {
                    "id": 8,
                    "valor": "BONOS DEL TESORO EEUU"
                },
                {
                    "id": 9,
                    "valor": "TES IPC"
                },
                {
                    "id": 10,
                    "valor": "DOLAR"
                }
            ],
            "titulos": [
                {
                    "id": 1,
                    "idtitulo": 1,
                    "titulo": 1,
                    "clasificacion": "DIV",
                    "valor": 5000000,
                    "fecha_de_creacion": "2022-03-14",
                    "fecha_de_vencimiento": "2023-03-15",
                    "pagocuota": "y"
                },
                {
                    "id": 2,
                    "idtitulo": 2,
                    "titulo": 2,
                    "clasificacion": "",
                    "valor": 256000000,
                    "fecha_de_creacion": "2022-08-25",
                    "fecha_de_vencimiento": "2023-08-26",
                    "pagocuota": "y"
                },
                {
                    "id": 3,
                    "idtitulo": 3,
                    "titulo": 2,
                    "clasificacion": "",
                    "valor": 360000000,
                    "fecha_de_creacion": "2022-02-16",
                    "fecha_de_vencimiento": "2023-02-17",
                    "pagocuota": "y"
                }
            ]
        }

        with open(self.connection_string, 'w') as json_file:
            json.dump(self.data, json_file)

    def test_obtener(self):
        bd = BaseDeDatos(self.connection_string)
        result = bd.obtener()
        self.assertEqual(result, self.data)


if __name__ == '__main__':
    unittest.main()
