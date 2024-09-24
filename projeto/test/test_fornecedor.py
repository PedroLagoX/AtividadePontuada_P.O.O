from projeto.models.classes.endereco import Endereco
from projeto.models.classes_que_estendem_juridica.fornecedor import Fornecedor
from projeto.models.enums.unidadefederativa import Unidadefederativa
import pytest


@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua D", "31", "300","2993829", "Salvador", Unidadefederativa.BAHIA)
    return endereco

@pytest.fixture
def fornecedor_valido(endereco_valido):
    fornecedor = Fornecedor("12039013","Julia","98188221","juliavales@email",endereco_valido,"123456","239193231","Sabão")
    return fornecedor

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.nome == "Julia"    

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.id == "12039013"

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.cnpj == "123456"    

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.telefone == "98188221"     

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.email == "juliavales@email"    

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual == "239193231"

def test_validando_atributos_nome(fornecedor_valido):
    assert fornecedor_valido.produto == "Sabão"  

def test_validando_atributos_pessoa_logradouro(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro == "Rua D"

def test_validando_atributos_pessoa_numero(fornecedor_valido):
    assert fornecedor_valido.endereco.numero == "31"

def test_validando_atributos_pessoa_complemento(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento == "300"

def test_validando_atributos_pessoa_cep(fornecedor_valido):
    assert fornecedor_valido.endereco.cep == "2993829"

def test_validando_atributos_pessoa_cidade(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "Salvador"

def test_validando_atributos_pessoa_uf(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == Unidadefederativa.BAHIA  