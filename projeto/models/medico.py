from projeto.models.endereco import Endereco
from projeto.models.enums.estadocivil import Estado_Civil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: Estado_Civil, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm:str) -> None:
        super().__init__(nome, telefone, email, endereco, dataNascimento, genero, estadocivil, cpf, rg, matricula, setor, salario)

        self.crm = crm

    def __str__(self) -> str:
        return (f"{super().__str__()},\nCRM:{self.crm}")