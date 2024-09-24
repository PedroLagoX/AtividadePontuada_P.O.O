from projeto.models.classes_que_estendem_pessoa.fisica import Fisica
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil
import pytest

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua B", "42", "700", "120293023", "Salvador", Unidadefederativa.BAHIA)
    return endereco

@pytest.fixture
def fisica_valida(endereco_valido):
    fisica = Fisica(
        "9283932",
        "Pedro",
        "92398921",
        "pedrolago@email",
        endereco_valido,  # Corrigido para usar a instância do endereço
        "20/1973",
        Genero.MASCULINO,
        EstadoCivil.SOLTEIRO
    )
    return fisica

def test_validando_atributos_nome(fisica_valida):
    assert fisica_valida.nome == "Pedro"

def test_validando_atributos_id(fisica_valida):
    assert fisica_valida.id == "9283932"

def test_validando_atributos_telefone(fisica_valida):
    assert fisica_valida.telefone == "92398921"

def test_validando_atributos_email(fisica_valida):
    assert fisica_valida.email == "pedrolago@email"

def test_validando_atributos_pessoa_logradouro(fisica_valida):
    assert fisica_valida.endereco.logradouro == "Rua B"

def test_validando_atributos_pessoa_numero(fisica_valida):
    assert fisica_valida.endereco.numero == "42"

def test_validando_atributos_pessoa_complemento(fisica_valida):
    assert fisica_valida.endereco.complemento == "700"

def test_validando_atributos_pessoa_cep(fisica_valida):
    assert fisica_valida.endereco.cep == "120293023"

def test_validando_atributos_pessoa_cidade(fisica_valida):
    assert fisica_valida.endereco.cidade == "Salvador"

def test_validando_atributos_pessoa_uf(fisica_valida):
    assert fisica_valida.endereco.uf == Unidadefederativa.BAHIA

def test_validando_atributos_pessoa_dataNascimento(fisica_valida):
    assert fisica_valida.dataNascimento == "20/1973"  # Acessar diretamente no objeto Fisica

def test_validando_atributos_pessoa_genero(fisica_valida):
    assert fisica_valida.genero == Genero.MASCULINO  # Acessar diretamente no objeto Fisica

def test_validando_atributos_pessoa_estadocivil(fisica_valida):
    assert fisica_valida.estadocivil == EstadoCivil.SOLTEIRO 
   


   

        