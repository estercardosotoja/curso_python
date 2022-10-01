import unittest
from Aula118_Unittest import converte_padrao, par_impar


# É bom nomear as classes com o mesmo nome do módulo testado
class ConhecendoUnittestTeste(unittest.TestCase):
    # Recebe self porque a classe ConhecendoUnittestTeste herda de TestCase,
    # que por sua vez tem o método assertEqual, etc.
    def test_converte_padrao_tarde(self):
        """Teste para horarios vespertinos e noturnos"""
        self.assertEqual(converte_padrao(14, 25), '2:25 P.M', 'Deu Erro')

    def test_converte_padrao_manha(self):
        """Teste para horarios matutinos"""
        self.assertEqual(converte_padrao(8, 10), '8:10 A.M')

    def test_converte_padrao_retorno(self):
        """Teste o tipo do retorno da função"""
        self.assertIs(type(converte_padrao(8, 10)), str)

    def test_par_impar_par(self):
        """Teste para saber se é par"""
        self.assertTrue(par_impar(4))

    # Caso teste, vai dar como passado, porque assertFalse testa: bool(None)
    def test_par_impar_impar(self):
        # is False e não a identidade None == False
        """Teste para saber se é impar"""
        self.assertFalse(par_impar(5))

# Essa linha é necessaria pois podemos importar o módulo testes(reaproveitando para outros sistemas) e assim,
# não realizar os testes toda vez que executar o programa que o importou.


if __name__ == '__main__':
    # Comando para criar a inteface e realizar os testes em si
    unittest.main()
