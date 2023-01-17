from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin

@dataclass(frozen=True)

class DTOTitulo(JsonSchemaMixin):
    id:int
    idtitulo: int
    titulo: int
    clasificacion: str
    valor: int
    fecha_de_creacion: str
    fecha_de_vencimiento: str
    pagocuota: str
