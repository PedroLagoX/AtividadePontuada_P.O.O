from enum import Enum

class Setor(Enum):
    ENGENHARIA = ("Engenharia")
    SAUDE = ("Saúde")
    JURIDICO = ("Jurídico")
    OPERACOES = ("Operações")
    
    def __init__(self, nome) -> None:
        self.nome = nome