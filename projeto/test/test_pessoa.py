import pytest
from projeto.models.classes_abstratas.pessoa import Pessoa
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa


@pytest.fixture
def endereco_valido():
    
        endereco=Endereco("Rua A","41","800","182382123","Salvador",Unidadefederativa.BAHIA)
        return endereco
   
        
@pytest.fixture
def pessoa_valida(endereco_valido):
  
        pessoa=Pessoa("19282893","Julio Cesar","982873750","juliocesar@",endereco_valido)
        return pessoa
    

def test_validando_atributos_pessoa(pessoa_valida):
    assert pessoa_valida.nome=="Julio Cesar"

def test_validando_atributos_id(pessoa_valida):
    assert pessoa_valida.id=="19282893"

def test_validando_atributos_telefone(pessoa_valida):
    assert pessoa_valida.telefone=="982873750"

def test_validando_atributos_email(pessoa_valida):
    assert pessoa_valida.email=="juliocesar@"

def test_validando_atributos_pessoa_logradouro(pessoa_valida):
    assert pessoa_valida.endereco.logradouro=="Rua A"

def test_validando_atributos_pessoa_numero(pessoa_valida):
    assert pessoa_valida.endereco.numero=="41"

def test_validando_atributos_pessoa_complemento(pessoa_valida):
    assert pessoa_valida.endereco.complemento=="800"

def test_validando_atributos_pessoa_cep(pessoa_valida):
    assert pessoa_valida.endereco.cep=="182382123"
    
def test_validando_atributos_pessoa_cidade(pessoa_valida):
    assert pessoa_valida.endereco.cidade=="Salvador"

def test_validando_atributos_pessoa_uf(pessoa_valida):
    assert pessoa_valida.endereco.uf==Unidadefederativa.BAHIA

    
   



