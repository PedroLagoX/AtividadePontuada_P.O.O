import pytest
from projeto.models.classes_que_estendem_funcionario.medico import Medico
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.setor import Setor

@pytest.fixture
def endereco_valido():
    return Endereco("Rua C", "32", "600", "20223121", "Salvador", Unidadefederativa.BAHIA)

@pytest.fixture
def medico_valido(endereco_valido):
    return Medico(
        "19282893", "Julio Cesar", "982873750", "juliocesar@", 
        endereco_valido, "14/2005", Genero.MASCULINO, 
        EstadoCivil.SOLTEIRO, "92923819", "88283813", 
        "1828218321", Setor.ENGENHARIA, 50000,"1234567"
    )
def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.nome == "Julio Cesar"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.id == "19282893"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.telefone== "982873750"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.email == "juliocesar@"
    
def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.dataNascimento == "14/2005"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.cpf == "92923819"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.rg == "88283813"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.matricula == "1828218321"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.genero == Genero.MASCULINO

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.estadocivil == EstadoCivil.SOLTEIRO

def test_validando_atributos_salario_negativo(endereco_valido):
    with pytest.raises(ValueError, match="Salário não pode ser negativo."):
        Medico("19282893", "Julio Cesar", "982873750", "juliocesar@", 
                    endereco_valido, "14/2005", Genero.MASCULINO, 
                    EstadoCivil.SOLTEIRO, "92923819", "88283813", 
                    "1828218321", Setor.ENGENHARIA, -50000,"1234567")
        
def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.endereco.logradouro == "Rua C"
  
def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.endereco.numero == "32"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.endereco.complemento == "600"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.endereco.uf == Unidadefederativa.BAHIA

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.cidade == "Salvador"

def test_validando_atributos_pessoa(medico_valido):
    assert medico_valido.crm == "1234567"