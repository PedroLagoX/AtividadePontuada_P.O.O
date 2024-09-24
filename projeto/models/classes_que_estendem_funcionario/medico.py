from projeto.models.classes.endereco import Endereco
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.classes_abstratas.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, id:str ,nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: EstadoCivil, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm:str) -> None:
        super().__init__(id,nome, telefone, email, endereco, dataNascimento, genero, estadocivil, cpf, rg, matricula, setor, salario)

        self.crm = self.__verificar_crm(crm)

    def __verificar_crm(self, crm):
        try:
            if not crm:
                raise ValueError("CRM não pode estar vazio")
            if not isinstance(crm, str):
                raise TypeError("CRM só pode ser uma string")
            return crm
        
        except(ValueError,TypeError) as erro:
                print(erro)

    def __str__(self) -> str:
        return (f"{super().__str__()},\nCRM:{self.crm}")