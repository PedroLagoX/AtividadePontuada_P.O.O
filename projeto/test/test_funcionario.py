import pytest

import pytest
from projeto.models.classes_abstratas.pessoa import Funcionario
from projeto.models.classes.endereco import Endereco
from projeto.models.enums.unidadefederativa import Unidadefederativa
from projeto.models.enums.genero import Genero
from projeto.models.enums.estadocivil import EstadoCivil
from projeto.models.enums.setor import Setor



@pytest.fixture
def endereco_valido():
    
        endereco=Endereco("Rua C","32","600","2O223121","Salvador",Unidadefederativa.BAHIA)
        return endereco
   
        
@pytest.fixture
def funcionario_valido(endereco_valido):
  
        funcionario=Funcionario("19282893","Julio Cesar","982873750","juliocesar@",endereco_valido,"12/1500",Genero.MASCULINO,EstadoCivil.SOLTEIRO,"92923819","88283813","1828218321",Setor.ENGENHARIA, 50000)
        return funcionario
    

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
    
def test_validando_atributos_pessoa_setor(pessoa_valida):
    assert pessoa_valida.endereco.setor==Setor.ENGENHARIA
def test_validando_atributos_pessoa_salario(pessoa_valida):
    assert pessoa_valida.endereco.salario==50000

def test_validando_atributos_pessoa_matricula(pessoa_valida):
    assert pessoa_valida.endereco.matricula=="1828218321"

def test_validando_atributos_pessoa_cpf(pessoa_valida):
    assert pessoa_valida.cpf== "92923819"

def test_validando_atributos_pessoa_rg(pessoa_valida):
    assert pessoa_valida.endereco.rg=="88283813"

   
   