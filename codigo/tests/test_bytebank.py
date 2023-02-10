from bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 23

        
        funcionario_teste = Funcionario('Teste',entrada, 1111)
        # WHEN - Ação
        resultado = funcionario_teste.idade()

        # Then-desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_carvalho(self):
        entrada = ' Lucas Carvalho ' #Given
        esperado = 'Carvalho' 

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/20000', entrada_salario) 
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def teste_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        entrada_nome = 'Paulo Bragança'
        esperado = 100

        funcionario_teste = Funcionario(entrada_nome, '11/11/20000', entrada_salario) 
        
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000
            entrada_nome = 'Paulo Bragança'
            
            funcionario_teste = Funcionario(entrada_nome, '11/11/20000', entrada_salario) 
            resultado = funcionario_teste.calcular_bonus()

            assert resultado 