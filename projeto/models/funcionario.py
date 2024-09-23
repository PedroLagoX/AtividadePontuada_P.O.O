from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.enums.genero import Genero
from projeto.models.fisica import Fisica
from projeto.models.enums.estadocivil import Estado_Civil
from projeto.models.enums.setor import Setor

class Funcionario(Fisica,ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: Estado_Civil,cpf:str,rg:str,matricula:str,setor:Setor,salario:float) -> None:
        super().__init__(nome, telefone, email, endereco, dataNascimento, genero, estadocivil)

        self.cpf=cpf
        self.rg=rg
        self.matricula=matricula
        self.setor=setor
        self.salario=salario

    def __str__(self) -> str:
        return (f"{super().__str__()},\nCPF: {self.cpf},\nRG: {self.rg},\nMatricula: {self.matricula},\nSetor:{self.setor},\nSalario:{self.salario}")