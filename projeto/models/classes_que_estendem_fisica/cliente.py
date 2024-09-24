
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.genero import Genero
from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.enums.estadocivil import EstadoCivil

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: EstadoCivil,protocoloAtendimento:int) -> None:
        super().__init__(nome, telefone, email, endereco, dataNascimento, genero, estadocivil)

        self.protocoloAtendimento=protocoloAtendimento

    def __str__(self) -> str:
        return (f"{super().__str__()},\nProtocolo de Atendimento:{self.protocoloAtendimento}")