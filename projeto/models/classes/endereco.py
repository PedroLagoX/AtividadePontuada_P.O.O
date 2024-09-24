from projeto.models.enums.unidadefederativa import Unidadefederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: Unidadefederativa) -> None:
        self.logradouro = self.__verificar_logradouro(logradouro)
        self.numero = self.__verificar_numero(numero)
        self.complemento = self.__verificar_complemento(complemento)
        self.cep = self.__verificar_cep(cep)
        self.cidade = self.__verificar_cidade(cidade)
        self.uf = self.__verificar_uf(uf)

    def __verificar_logradouro(self, logradouro):
        try:
            if not logradouro:
                raise ValueError("Logradouro não pode estar vazio")
            
            if not isinstance(logradouro, str):
                raise TypeError("Logradouro só pode ser uma string")
            
            return logradouro
        
        except(TypeError,ValueError) as erro:
            print(erro)

    def __verificar_numero(self, numero):
        try:
            if not numero:
                raise ValueError("Número não pode estar vazio")
            if not isinstance(numero, str):
                raise TypeError("Número só pode ser uma string")
            return numero
        except(ValueError,TypeError) as erro:
            print(erro)

    def __verificar_complemento(self, complemento):
        try:
            if not complemento:
                raise ValueError("Complemento não pode estar vazio")
            
            if not isinstance(complemento, str):
                raise TypeError("Complemento só pode ser uma string")
            
            return complemento

        except(ValueError,TypeError) as erro:
            print(erro)

    def __verificar_cep(self, cep):
        try:
            if not cep:
                raise ValueError("CEP não pode estar vazio")
            
            if not isinstance(cep, str):
                raise TypeError("CEP só pode ser uma string")
            return cep
        except(TypeError,ValueError) as erro:
            print(erro)

    def __verificar_cidade(self, cidade):
        try:
            if not cidade:
                raise ValueError("Cidade não pode estar vazio")
            if not isinstance(cidade, str):
                raise TypeError("Cidade só pode ser uma string")
            return cidade
        except(ValueError,TypeError) as erro:
            print(erro)
    def __verificar_uf(self, uf):
        try:
            if not uf:
                raise ValueError("Unidade Federativa não pode estar vazio")
            if not isinstance(uf, Unidadefederativa):
                raise TypeError("Unidade Federativa está incorreta")
            return uf
        
        except(TypeError,ValueError) as erro:
            print(erro)