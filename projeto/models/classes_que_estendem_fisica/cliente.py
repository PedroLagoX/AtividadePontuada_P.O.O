
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.genero import Genero
from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.enums.estadocivil import EstadoCivil

class Cliente(Fisica):
    def __init__(self,id:str, nome: str, telefone: str, email: str, endereco: Endereco, dataNascimento: str, genero: Genero, estadocivil: EstadoCivil,protocoloAtendimento:int) -> None:
        super().__init__(id,nome, telefone, email, endereco, dataNascimento, genero, estadocivil)

        self.protocoloAtendimento=self.__verificar_protocoloAtendimento(protocoloAtendimento)

    def __verificar_protocoloAtendimento(self,protocoloAtendimento):
        try:
            if not protocoloAtendimento:
                raise ValueError('Protocolo de Atendimento não pode estar vazio')
            if  not isinstance(protocoloAtendimento,int):
                raise TypeError("Protocolo de Atendimento só pode ser um numero inteiro")
            return protocoloAtendimento
        except(ValueError,TypeError) as erro:
            print(erro)

    def __str__(self) -> str:
        return (f"{super().__str__()},\nProtocolo de Atendimento:{self.protocoloAtendimento}")