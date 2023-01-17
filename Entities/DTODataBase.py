from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin
from . import *

@dataclass(frozen=True)

class DTODataBase(JsonSchemaMixin):
    id_titulos: list[DTOIdTitulo]
    titulos_preestablecidos: list[DTOTituloPrestablecido]
    titulos: list[DTOTitulo]
