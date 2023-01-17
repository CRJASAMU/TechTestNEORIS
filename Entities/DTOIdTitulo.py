from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin

@dataclass(frozen=True)

class DTOIdTitulo(JsonSchemaMixin):
    id: int
    name: str

