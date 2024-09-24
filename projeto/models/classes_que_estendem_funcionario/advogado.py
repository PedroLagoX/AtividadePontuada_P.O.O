from projeto.models.classes.endereco import Endereco
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.classes_abstratas.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self,id:str, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: EstadoCivil, cpf: str, rg: str, matricula: str, setor: Setor, salario: float,oab:str) -> None:
        super().__init__(id,nome, telefone, email, endereco, dataNascimento, genero, estadocivil, cpf, rg, matricula, setor, salario)

        self.oab=self.__verificar_oab(oab)

    def __verificar_oab(self, oab):
        try:
            if not oab:
                raise ValueError("OAB não pode estar vazio")
            if not isinstance(oab, str):
                raise TypeError("OAB só pode ser uma string")
            return oab
    
        except(ValueError,TypeError) as erro:
                print(erro)

    def __str__(self) -> str:
        return (f"{super().__str__()},\nOAB:{self.oab}")