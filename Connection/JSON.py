import json
from Entities import DTODataBase
from jsonschema import validate


class BaseDeDatos:
    def __init__(self, connection_string: str):
        self.file_path = connection_string

    def obtener(self):
        with open(self.file_path, 'r') as json_file:
            json_data: DTODataBase = json.load(json_file)
            return json_data

    def actualizar(self, new_data: DTODataBase):
        with open(self.file_path, 'r') as json_file:
            validate(instance=new_data, schema=DTODataBase.json_schema())
            json_data: DTODataBase = json.load(json_file)
            json_data = new_data
        with open(self.file_path, 'w') as json_file:
            json.dump(json_data, json_file)
