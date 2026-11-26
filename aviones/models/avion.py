"""Esta clase modela los datos de un avion"""
from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Avion:
    aerolinea: str
    modelo: str
    capacidad: int
    destino: str
    uuid: UUID = field(default_factory=uuid4)