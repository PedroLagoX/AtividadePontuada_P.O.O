import pytest
from projeto.models.classes_que_estendem_fisica.cliente import Cliente
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil


@pytest.fixture
def endereco_valido():
    return Endereco("Rua C", "32", "600", "20223121", "Salvador", Unidadefederativa.BAHIA)

@pytest.fixture
def cliente_valido(endereco_valido):
    return Cliente(
        "19282893", "Julio Cesar", "982873750", "juliocesar@", 
        endereco_valido, "14/2005", Genero.MASCULINO, 
        EstadoCivil.SOLTEIRO,12345
    )
def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.nome == "Julio Cesar"

def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.id == "19282893"

def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.telefone == "982873750"

def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.email== "juliocesar@"

def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.dataNascimento == "14/2005"



def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.genero == Genero.MASCULINO

def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.estadocivil== EstadoCivil.SOLTEIRO


def test_validando_atributos_pessoa(cliente_valido):
    assert cliente_valido.protocoloAtendimento== 12345

    
def test_validando_atributos_endereco(cliente_valido):
    assert cliente_valido.endereco.logradouro == "Rua C"

def test_validando_atributos_numero(cliente_valido):
    assert cliente_valido.endereco.numero == "32"

def test_validando_atributos_complemento(cliente_valido):
    assert cliente_valido.endereco.complemento == "600"

def test_validando_atributos_uf(cliente_valido):
    assert cliente_valido.endereco.uf == Unidadefederativa.BAHIA

def test_validando_atributos_cidade(cliente_valido):
    assert cliente_valido.endereco.cidade == "Salvador"
    
