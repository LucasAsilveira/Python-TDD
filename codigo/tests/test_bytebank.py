from bytebank import Funcionario

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
