from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin

@dataclass(frozen=True)

class DTOTituloPrestablecido(JsonSchemaMixin):
    id: int
    valor: str

