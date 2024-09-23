from enum import Enum

class Genero(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

    def __init__(self, texto) -> None:
        self.texto = texto