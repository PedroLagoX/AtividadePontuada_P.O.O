from abc import ABC,abstractmethod
from projeto.models.classes.endereco import Endereco
from projeto.models.classes_abstratas.pessoa import Pessoa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil

class Fisica(Pessoa,ABC):
    def __init__(self,id:str, nome: str, telefone: str, email: str, endereco: Endereco,dataNascimento:str,genero:Genero,estadocivil:EstadoCivil) -> None:
        super().__init__(id,nome, telefone, email, endereco)

        
        self.dataNascimento=self.__verificar_dataNascimento(dataNascimento)
        self.genero=self.__verificar_enero(genero)
        self.estadocivil=self.__verificar_EstadoCivil(EstadoCivil) 

    def __verificar_dataNascimento(self, dataNascimento):
            try:
                if not dataNascimento:
                    raise ValueError("Data de Nascimento não pode estar vazia")
                if not isinstance(id, str):
                    raise TypeError("Data de Nascimento só pode ser uma string")
                return id
    
            except(ValueError,TypeError) as erro:
                print(erro)


    def __verificar_genero(self, genero):
        try:
            if not genero:
                raise ValueError("Genero não pode ser vazio")
            if not isinstance(genero, str):
                raise TypeError("Genero só pode ser uma string")
            return genero
        except(ValueError,TypeError) as erro:
            print(erro)

    def __verificar_estadocivil(self, EstadoCivil):
        try:
            if not EstadoCivil:
                raise ValueError("Telefone não pode estar vazio")
            if not isinstance(EstadoCivil, str):
                raise TypeError("Telefone só pode ser uma string")
            return EstadoCivil
        
        except(ValueError,TypeError) as erro:
            print(erro)

    def __str__(self) -> str:
        return (f"{super().__str__()},\nData de Nascimento:{self.dataNascimento},\nGenero:{self.genero},\nEstado Civil: {self.estadocivil}")
    



        