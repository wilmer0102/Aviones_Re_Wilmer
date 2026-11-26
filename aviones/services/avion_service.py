"""Contiene la lógica de negocio de mi aplicación."""
from uuid import UUID
from models.avion import Avion
from repositories.avion_repository import AvionRepository

class AvionService:
    def __init__(self, repository: AvionRepository) -> None:
        self.repository = repository

    def find_all(self):
        return self.repository.find_all()

    def create_one(self, aerolinea: str, modelo: str, capacidad: int, destino: str):
        avion = Avion(aerolinea, modelo, capacidad, destino)
        self.repository.create_one(avion)

    def delete_one(self, uuid: UUID):
        self.repository.delete_one(uuid)

    def update_one(self, uuid: UUID, aerolinea: str, modelo: str, capacidad: int, destino: str):
        self.repository.update_one(uuid, aerolinea, modelo, capacidad, destino)