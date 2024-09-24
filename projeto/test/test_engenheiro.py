from projeto.models.classes.endereco import Endereco
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.classes_que_estendem_funcionario.engenheiro import Engenheiro
import pytest

@pytest.fixture
def endereco_valido():
    return Endereco("Rua E","42","900","9182329","Salvador",Unidadefederativa.BAHIA)

@pytest.fixture
def engenheiro_valido(endereco_valido):
    return Engenheiro(
        "19282893", "Julio Cesar", "982873750", "juliocesar@", 
        endereco_valido, "14/2005", Genero.MASCULINO, 
        EstadoCivil.SOLTEIRO, "92923819", "88283813", 
        "1828218321", Setor.ENGENHARIA, 50000,"123456"
    )
def test_validando_atributos_pessoa(engenheiro_valido):
    assert engenheiro_valido.nome == "Julio Cesar"

def test_validando_atributos_id(engenheiro_valido):
    assert engenheiro_valido.id == "19282893"

def test_validando_atributos_telefone(engenheiro_valido):
    assert engenheiro_valido.telefone == "982873750"

def test_validando_atributos_email(engenheiro_valido):
    assert engenheiro_valido.email == "juliocesar@"

def test_validando_atributos_dataNascimento(engenheiro_valido):
    assert engenheiro_valido.dataNascimento == "14/2005"

def test_validando_atributos_cpf(engenheiro_valido):
    assert engenheiro_valido.cpf == "92923819"

def test_validando_atributos_rg(engenheiro_valido):
    assert engenheiro_valido.rg == "88283813"

def test_validando_atributos_matricula(engenheiro_valido):
    assert engenheiro_valido.matricula == "1828218321"

def test_validando_atributos_genero(engenheiro_valido):
    assert engenheiro_valido.genero == Genero.MASCULINO

def test_validando_atributos_estadocivil(engenheiro_valido):
    assert engenheiro_valido.estadocivil == EstadoCivil.SOLTEIRO

def test_validando_atributos_salario_negativo(endereco_valido):
    with pytest.raises(ValueError, match="Salário não pode ser negativo."):
        Engenheiro("19282893", "Julio Cesar", "982873750", "juliocesar@", 
                    endereco_valido, "14/2005", Genero.MASCULINO, 
                    EstadoCivil.SOLTEIRO, "92923819", "88283813", 
                    "1828218321", Setor.ENGENHARIA, -50000,"123456")  # Salário negativo

def test_validando_atributos_salario(engenheiro_valido):
    assert engenheiro_valido.salario == 50000

def test_validando_atributos_setor(engenheiro_valido):
    assert engenheiro_valido.setor ==  Setor.ENGENHARIA

def test_validando_atributos_endereco(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Rua E"

def test_validando_atributos_numero(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "42"

def test_validando_atributos_complemento(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "900"

def test_validando_atributos_uf(engenheiro_valido):
    assert engenheiro_valido.endereco.uf == Unidadefederativa.BAHIA

def test_validando_atributos_cidade(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "Salvador"

def test_validando_atributos_crea(engenheiro_valido):
    assert engenheiro_valido.crea == "123456"