from projeto.models.classes.endereco import Endereco
from projeto.models.classes_que_estendem_pessoa.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self,id:str, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto:str) -> None:
        super().__init__(id,nome, telefone, email, endereco, cnpj, inscricaoEstadual)
    
        self.produto = self.__verificar_produto(produto)

    def __verificar_produto(self,produto):
        try:
            if not produto:
                raise ValueError("Produto não pode estar vazio")

            if not isinstance(produto,str):
                raise TypeError("O produto tem que ser uma string")
            return produto
        except(ValueError,TypeError) as erro:
            print(erro)

    def __str__(self) -> str:
        return (f"{super().__str__()},\nProduto:{self.produto}")