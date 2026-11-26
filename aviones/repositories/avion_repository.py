from typing import List
from uuid import UUID
from models.avion import Avion

class AvionRepository:
    _aviones: List[Avion] = [
        Avion("Arajet", "Boeing 737", 180, "Santo Domingo"),
        Avion("American Airlines", "Airbus A320", 150, "Miami"),
        Avion("Copa Airlines", "Boeing 737", 160, "Panama"),
    ]

    def __init__(self) -> None:
        pass

    def find_all(self) -> List[Avion]:
        return self._aviones

    def create_one(self, avion: Avion):
        self._aviones.append(avion)

    def delete_one(self, uuid: UUID):
        avion = [avion for avion in self._aviones if avion.uuid != uuid]
        self._aviones = avion

    def update_one(self, uuid: UUID, aerolinea: str, modelo: str, capacidad: int, destino: str):
        avion = [avion for avion in self._aviones if avion.uuid == uuid]

        if avion:
            avion[0].aerolinea = aerolinea
            avion[0].modelo = modelo
            avion[0].capacidad = capacidad
            avion[0].destino = destino