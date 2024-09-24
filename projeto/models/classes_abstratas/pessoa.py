from abc import ABC
from projeto.models.classes.endereco import Endereco

class Pessoa:
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self.__verificar_id(id)
        self.nome = self.__verificar_nome(nome)
        self.telefone = self.__verificar_telefone(telefone)
        self.email = self.__verificar_email(email)
        self.endereco = self.__verificar_endereco(endereco)  # Assumindo que o Endereco já faz suas próprias verificações

    def __verificar_id(self, id):
            try:
                if not id:
                    raise ValueError("ID não pode estar vazio")
                if not isinstance(id, str):
                    raise TypeError("ID só pode ser uma string")
                return id
    
            except(ValueError,TypeError) as erro:
                print(erro)


    def __verificar_nome(self, nome):
        try:
            if not nome:
                raise ValueError("Nome não pode ser vazio")
            if not isinstance(nome, str):
                raise TypeError("Nome só pode ser uma string")
            return nome
        except(ValueError,TypeError) as erro:
            print(erro)

    def __verificar_telefone(self, telefone):
        try:
            if not telefone:
                raise ValueError("Telefone não pode estar vazio")
            if not isinstance(telefone, str):
                raise TypeError("Telefone só pode ser uma string")
            return telefone
        except(ValueError,TypeError) as erro:
            print(erro)


    def __verificar_email(self, email):
        try:
            if not email:
                raise ValueError("Email não pode estar vazio")
            if not isinstance(email, str):
                raise TypeError("Email só pode ser uma string")
            return email
        except(ValueError,TypeError) as erro:
            print(erro)
    


    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço: {self.endereco}"  # Aqui assume que Endereco já tem __str__ implementado
        )




  
    