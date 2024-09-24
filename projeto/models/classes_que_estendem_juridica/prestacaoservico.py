from projeto.models.classes.endereco import Endereco
from projeto.models.classes_que_estendem_pessoa.juridica import Juridica

class Prestacaoservico(Juridica):
    def __init__(self, id:str,nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoinicio:str, contratofinal:str) -> None:
        super().__init__(id,nome, telefone, email, endereco, cnpj, inscricaoEstadual)

        self.contratoinicio = self.__verificar_contratoinicio(contratoinicio)
        self.contratofinal = self.__verificar_contratofinal(contratofinal)

    def __verificar_contratoinicio(self,contratoinicio):
        try:
            if not contratoinicio:
                raise ValueError("O inicio do contrato não pode estar vazio")

            if not isinstance(contratoinicio,str):
                raise TypeError("O inicio do contrato tem que ser uma string")
            return contratoinicio
        except(ValueError,TypeError) as erro:
            print(erro)
    
    def __verificar_contratofinal(self,contratofinal):
        try:
            if not contratofinal:
                raise ValueError("O final do contrato não pode estar vazio")

            if not isinstance(contratofinal,str):
                raise TypeError("O final do contrato tem que ser uma string")
            return contratofinal
        
        except(ValueError,TypeError) as erro:
            print(erro)
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, \nContrato Inicio:{self.contratoinicio},\nContrato Final: {self.contratofinal}")