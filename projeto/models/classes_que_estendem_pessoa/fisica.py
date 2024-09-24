from abc import ABC,abstractmethod
from projeto.models.classes.endereco import Endereco
from projeto.models.classes_abstratas.pessoa import Pessoa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil

class Fisica(Pessoa, ABC):
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: EstadoCivil) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        
        self.dataNascimento = self.__verificar_dataNascimento(dataNascimento)
        self.genero = self.__verificar_genero(genero)
        self.estadocivil = self.__verificar_estadocivil(estadocivil)

    def __verificar_dataNascimento(self, dataNascimento):
        try:
            if not dataNascimento:
                raise ValueError("Data de Nascimento não pode estar vazia")
            if not isinstance(dataNascimento, str):
                raise TypeError("Data de Nascimento só pode ser uma string")
            return dataNascimento
        except (ValueError, TypeError) as erro:
            print(erro)

    def __verificar_genero(self, genero):
        try:
            if not isinstance(genero, Genero):
                raise TypeError("Gênero está incorreto")
            return genero
        except TypeError as erro:
            print(f"Erro ao verificar gênero: {erro}")

    def __verificar_estadocivil(self, estadocivil):
        try:
            if not isinstance(estadocivil, EstadoCivil):
                raise TypeError("Estado Civil está incorreto")
            return estadocivil
        except TypeError as erro:
            print(erro)

    def __str__(self) -> str:
        return (f"{super().__str__()},\nData de Nascimento: {self.dataNascimento},\nGênero: {self.genero},\nEstado Civil: {self.estadocivil}")