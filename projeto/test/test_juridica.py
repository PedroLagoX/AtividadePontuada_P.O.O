from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.classes_que_estendem_pessoa.juridica import Juridica
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil
import pytest

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua D", "31", "300","2993829", "Salvador", Unidadefederativa.BAHIA)
    return endereco

@pytest.fixture
def juridica_valida(endereco_valido):
    juridica = Juridica("12039013","Julia","98188221","juliavales@email",endereco_valido,"239193231","139291032")
    return juridica
    

def test_validando_atributos_nome(juridica_valida):
    assert juridica_valida.nome == "Julia"

def test_validando_atributos_id(juridica_valida):
    assert juridica_valida.id == "12039013"

def test_validando_atributos_telefone(juridica_valida):
    assert juridica_valida.telefone == "98188221"

def test_validando_atributos_email(juridica_valida):
    assert juridica_valida.email == "juliavales@email"

def test_validando_atributos_pessoa_logradouro(juridica_valida):
    assert juridica_valida.endereco.logradouro == "Rua D"

def test_validando_atributos_pessoa_numero(juridica_valida):
    assert juridica_valida.endereco.numero == "31"

def test_validando_atributos_pessoa_complemento(juridica_valida):
    assert juridica_valida.endereco.complemento == "300"

def test_validando_atributos_pessoa_cep(juridica_valida):
    assert juridica_valida.endereco.cep == "2993829"

def test_validando_atributos_pessoa_cidade(juridica_valida):
    assert juridica_valida.endereco.cidade == "Salvador"

def test_validando_atributos_pessoa_uf(juridica_valida):
    assert juridica_valida.endereco.uf == Unidadefederativa.BAHIA

def test_validando_atributos_pessoa_inscricaoEstadual(juridica_valida):
    assert juridica_valida.inscricaoEstadual =="139291032"  


   


   

        