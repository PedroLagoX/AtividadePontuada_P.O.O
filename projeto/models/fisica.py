from abc import ABC,abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil

class Fisica(Pessoa,ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,dataNascimento:str,genero:Genero,estadocivil:EstadoCivil) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.dataNascimento=dataNascimento
        self.genero=genero 
        self.estadocivil=estadocivil 

    def __str__(self) -> str:
        return (f"{super().__str__()},\nData de Nascimento:{self.dataNascimento},\nGenero:{self.genero},\nEstado Civil: {self.estadocivil}")
    



        