from projeto.models.classes.endereco import Endereco
from projeto.models.classes_que_estendem_juridica.prestacaoservico import Prestacaoservico
from projeto.models.enums.unidadefederativa import Unidadefederativa
import pytest


@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua D", "31", "300","2993829", "Salvador", Unidadefederativa.BAHIA)
    return endereco

@pytest.fixture
def prestacao_servico_valido(endereco_valido):
    prestacaoservico = Prestacaoservico("12039013","Julia","98188221","juliavales@email",endereco_valido,"123456","14/03/2005","24/09/2024")
    return prestacaoservico

def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.nome == "Julia"    

def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.id== "12039013"    

def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.telefone == "98188221"

def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.email == "juliavales@gmail"

def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.contratoinicio == "14/03/2005"

def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.contratofinal == "24/09/2024"    

    
def test_validando_atributos_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.inscricaoEstadual == "123456"


def test_validando_atributos_pessoa_logradouro(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.logradouro == "Rua D"

def test_validando_atributos_pessoa_numero(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.numero == "31"

def test_validando_atributos_pessoa_complemento(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.complemento == "300"

def test_validando_atributos_pessoa_cep(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.cep == "2993829"

def test_validando_atributos_pessoa_cidade(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.cidade == "Salvador"

def test_validando_atributos_pessoa_uf(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.uf == Unidadefederativa.BAHIA  