from abc import ABC
from projeto.models.classes.endereco import Endereco
from projeto.models.classes_abstratas.pessoa import Pessoa

class Juridica(Pessoa,ABC):
   def __init__(self,id:str, nome: str, telefone: str, email: str, endereco: Endereco,cnpj:str,inscricaoEstadual:str) -> None:
      super().__init__(id,nome, telefone, email, endereco)
      
      self.cnpj=self.__verificar_cnpj(cnpj)
      self.inscricaoEstadual=self.__verificar_inscricaoEstadual(inscricaoEstadual)

   def __verificar_cnpj(self, cnpj):
      try:
         if not cnpj:
               raise ValueError("CNPJ não pode estar vazia")
         if not isinstance(cnpj, str):
               raise TypeError("CNPJ só pode ser uma string")
         return cnpj
    
      except(ValueError,TypeError) as erro:
         print(erro)


   def __verificar_inscricaoEstadual(self, inscricaoEstadual):
      try:
         if not inscricaoEstadual:
               raise ValueError("Inscrição Estadual não pode ser vazia")
         if not isinstance(inscricaoEstadual, str):
               raise TypeError("Inscrição Estadual só pode ser uma string")
         return inscricaoEstadual
      except(ValueError,TypeError) as erro:
            print(erro)
         
      def __str__(self) -> str:
         return (f"{super().__str__()},\nCNPJ:{self.cnpj},\nInscrição Estadual:{self.inscricaoEstadual}")