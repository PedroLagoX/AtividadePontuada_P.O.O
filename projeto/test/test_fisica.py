from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil
import pytest

@pytest.fixture
def endereco_valido():
    endereco=Endereco("Rua B","42","700","120293023","Salvador",Unidadefederativa.BAHIA)
    return endereco
    

@pytest.fixture
def fisica_valida():
    fisica=Fisica("9283932","Pedro","92398921","pedrolago@email",endereco_valido,"20/1973",Genero.MASCULINO,EstadoCivil.SOLTEIRO)

def test_validando_atributos_pessoa(pessoa_valida):
    assert pessoa_valida.nome=="Pedro"

def test_validando_atributos_id(pessoa_valida):
    assert pessoa_valida.id=="9283932"

def test_validando_atributos_telefone(pessoa_valida):
    assert pessoa_valida.telefone=="92398921"

def test_validando_atributos_email(pessoa_valida):
    assert pessoa_valida.email=="pedrolago@email"

def test_validando_atributos_pessoa_logradouro(pessoa_valida):
    assert pessoa_valida.endereco.logradouro=="Rua B"

def test_validando_atributos_pessoa_numero(pessoa_valida):
    assert pessoa_valida.endereco.numero=="42"

def test_validando_atributos_pessoa_complemento(pessoa_valida):
    assert pessoa_valida.endereco.complemento=="700"

def test_validando_atributos_pessoa_cep(pessoa_valida):
    assert pessoa_valida.endereco.cep=="182382123"
    
def test_validando_atributos_pessoa_cidade(pessoa_valida):
    assert pessoa_valida.endereco.cidade=="Salvador"

def test_validando_atributos_pessoa_uf(pessoa_valida):
    assert pessoa_valida.endereco.uf==Unidadefederativa.BAHIA

def test_validando_atributos_pessoa_dataNascimento(pessoa_valida):
    assert pessoa_valida.endereco.dataNascimento=="20/1973"

def test_validando_atributos_pessoa_genero(pessoa_valida):
    assert pessoa_valida.endereco.genero==Genero.MASCULINO

def test_validando_atributos_pessoa_estadocivil(pessoa_valida):
    assert pessoa_valida.endereco.EstadoCivil==EstadoCivil.Solteiro



    
   


   

        