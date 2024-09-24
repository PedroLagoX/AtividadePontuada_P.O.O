import pytest
from projeto.models.classes_abstratas.funcionario import Funcionario
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.setor import Setor

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua C", "32", "600", "20223121", "Salvador", Unidadefederativa.BAHIA)
    return endereco

@pytest.fixture
def funcionario_valido(endereco_valido):
    funcionario = Funcionario("19282893", "Julio Cesar", "982873750", "juliocesar@", endereco_valido, "14/2005", Genero.MASCULINO, EstadoCivil.SOLTEIRO, "92923819", "88283813", "1828218321", Setor.ENGENHARIA, 50000)
    return funcionario

def test_validando_atributos_pessoa(funcionario_valido):
    assert funcionario_valido.nome == "Julio Cesar"

def test_validando_atributos_id(funcionario_valido):
    assert funcionario_valido.id == "19282893"

def test_validando_atributos_telefone(funcionario_valido):
    assert funcionario_valido.telefone == "982873750"

def test_validando_atributos_email(funcionario_valido):
    assert funcionario_valido.email == "juliocesar@"

def test_validando_atributos_dataNascimento(funcionario_valido):
    assert funcionario_valido.dataNascimento == "14/2005"

def test_validando_atributos_cpf(funcionario_valido):
    assert funcionario_valido.cpf == "92923819"

def test_validando_atributos_rg(funcionario_valido):
    assert funcionario_valido.rg == "88283813"

def test_validando_atributos_matricula(funcionario_valido):
    assert funcionario_valido.matricula == "1828218321"

def test_validando_atributos_genero(funcionario_valido):
    assert funcionario_valido.genero == Genero.MASCULINO

def test_validando_atributos_estadocivil(funcionario_valido):
    assert funcionario_valido.estadocivil == EstadoCivil.SOLTEIRO

def test_validando_atributos_salario(funcionario_valido):
    assert funcionario_valido.salario == 50000

def test_validando_atributos_salario_negativo(endereco_valido):
    with pytest.raises(ValueError, match="Salário não pode ser negativo"):
        Funcionario("19282893", "Julio Cesar", "982873750", "juliocesar@", endereco_valido, "14/2005", Genero.MASCULINO, EstadoCivil.SOLTEIRO, "92923819", "88283813", "1828218321", Setor.ENGENHARIA, -1)

def test_validando_atributos_setor(funcionario_valido):
    assert funcionario_valido.setor == Setor.ENGENHARIA

def test_validando_atributos_endereco(funcionario_valido):
    assert funcionario_valido.endereco.logradouro == "Rua C"

def test_validando_atributos_numero(funcionario_valido):
    assert funcionario_valido.endereco.numero == "32"

def test_validando_atributos_complemento(funcionario_valido):
    assert funcionario_valido.endereco.complemento == "600"

def test_validando_atributos_uf(funcionario_valido):
    assert funcionario_valido.endereco.uf == Unidadefederativa.BAHIA

def test_validando_atributos_cidade(funcionario_valido):
    assert funcionario_valido.endereco.cidade == "Salvador"