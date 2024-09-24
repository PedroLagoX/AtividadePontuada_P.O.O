from abc import ABC
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.genero import Genero
from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.setor import Setor

class Funcionario(Fisica, ABC):
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco, 
                 dataNascimento: str, genero: Genero, estadocivil: EstadoCivil, 
                 cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, dataNascimento, genero, estadocivil)

        self.cpf = self.__verificar_cpf(cpf)
        self.rg = self.__verificar_rg(rg)
        self.matricula = self.__verificar_matricula(matricula)
        self.setor = self.__verificar_setor(setor)
        try:
            if salario <= 0:
                raise ValueError("Salário não pode ser negativo ou zero.")
            self.salario = salario
        except ValueError as erro:
            print(erro)
            raise  

        if salario <= 0:
            raise ValueError("Salário não pode ser negativo ou zero.")
        
        self.salario = salario
    
    def __verificar_cpf(self, cpf):
        if not cpf:
            raise ValueError("CPF não pode estar vazio.")
        if not isinstance(cpf, str):
            raise TypeError("CPF deve ser uma string.")
        return cpf
    
    def __verificar_setor(self, setor):
        if not setor:
            raise ValueError("Setor não pode estar vazio.")
        if not isinstance(setor, Setor):
            raise TypeError("Setor está incorreto.")
        return setor
    
    def __verificar_rg(self, rg):
        if not rg:
            raise ValueError("RG não pode ser vazio.")
        if not isinstance(rg, str):
            raise TypeError("RG deve ser uma string.")
        return rg
    
    def __verificar_matricula(self, matricula):
        if not matricula:
            raise ValueError("Matrícula não pode estar vazia.")
        if not isinstance(matricula, str):
            raise TypeError("Matrícula deve ser uma string.")
        return matricula
    
    def __str__(self) -> str:
        return (f"{super().__str__()},\n"
                f"CPF: {self.cpf},\n"
                f"RG: {self.rg},\n"
                f"Matrícula: {self.matricula},\n"
                f"Setor: {self.setor},\n"
                f"Salário: {self.salario}")