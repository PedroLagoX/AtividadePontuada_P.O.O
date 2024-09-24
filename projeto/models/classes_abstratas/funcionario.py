from abc import ABC
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.genero import Genero
from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.setor import Setor

class Funcionario(Fisica,ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: EstadoCivil,cpf:str,rg:str,matricula:str,setor:Setor,salario:float) -> None:
        super().__init__(nome, telefone, email, endereco, dataNascimento, genero, estadocivil)

        self.cpf=__verificar_cpf(cpf)
        self.rg=__verificar_rg(rg)
        self.matricula=__verificar_matricula(matricula)
        self.setor=__verificar_setor(setor)
        self.salario=__verificar_salario(salario)

        def __verificar_cpf(self,cpf):
            try:
                if not cpf:
                    raise ValueError("CPF não pode estar vazia")
                if not isinstance(cpf, str):
                    raise TypeError("CPF só pode ser uma string")
                return cpf
    
            except(ValueError,TypeError) as erro:
                print(erro)

        def __verificar_salario(self,salario):
            try:
                if not salario:
                    raise ValueError("Salário não pode estar vazio")
                if not isinstance(salario, str):
                    raise TypeError("Salário só pode ser um float")
                return salario
    
            except(ValueError,TypeError) as erro:
        
                print(erro)

        def __verificar_setor(self,salario):
            try:
                if not setor:
                    raise ValueError("Salário não pode estar vazio")
                if not isinstance(setor, str):
                    raise TypeError("Salário só pode ser um float")
                return salario
    
            except(ValueError,TypeError) as erro:
                print(erro)


        def __verificar_rg(self, rg):
            try:
                if not rg:
                    raise ValueError("RG não pode ser vazio")
                if not isinstance(rg, str):
                    raise TypeError("RG só pode ser uma string")
                return rg
            except(ValueError,TypeError) as erro:
                print(erro)

        def __verificar_matricula(self, matricula):
            try:
                if not matricula:
                    raise ValueError("Matrícula não pode estar vazio")
                if not isinstance(matricula, str):
                    raise TypeError("Matrícula só pode ser uma string")
                return EstadoCivil
            
            except(ValueError,TypeError) as erro:
                print(erro)


    def __str__(self) -> str:
        return (f"{super().__str__()},\nCPF: {self.cpf},\nRG: {self.rg},\nMatricula: {self.matricula},\nSetor:{self.setor},\nSalario:{self.salario}")