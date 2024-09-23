from projeto.models.endereco import Endereco
from projeto.models.juridica import Juridica

class Prestacaoservico(Juridica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoinicio:str, contratofinal:str) -> None:
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual)

        self.contratoinicio = contratoinicio
        self.contratofinal = contratofinal
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, \nContrato Inicio:{self.contratoinicio},\nContrato Final: {self.contratofinal}")