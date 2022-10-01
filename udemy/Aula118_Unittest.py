"""
Conhecendo Unittest

O que são?
 - Módulo para testar individualmente classes,funções, métodos, dentre outros.
Como trabalhar com ele?
 - Inicialmente importa-se o módulo unittest e criamos classes que herdam TestCase(Teste de caso) a partir desse módulo.
   Com isso é possível utilizar todos assertions contidos nele.
Tabela com todos assertions presentes no módulo: https://docs.python.org/pt-br/3/library/unittest.html#assert-methods
Apresentada abaixo:
assertEqual(a, b)    a == b

assertNotEqual(a, b)  a != b

assertTrue(x)        bool(x) is True

assertFalse(x)      bool(x) is False

assertIs(a, b)      a is b

assertIsNot(a, b)   a is not b

assertIsNone(x)     x is None

assertIsNotNone(x)  x is not None

assertIn(a, b)      a in b

assertNotIn(a, b)   a not in b

assertIsInstance(a, b)   isinstance(a, b)

assertNotIsInstance(a, b) not isinstance(a, b)
Ex:
->Aplicando TDD:
É convenção nomear cada função dentro do módulo teste iniciando com test_
É interessante que cada função tenha apenas um teste.
-> É possível adicionar docstrings nos testes, inclusive é recomendavel.
Obs: Existe um modo de abertura utilizando o -v, no qual apresenta mais detalhes dos testes.
Basta fazer no terminal: python nome_modulo_teste.py -v
"""
# Função que converte o padrão 24h para 12h.Ex: 16:34 -> 4:34 P.M


def converte_padrao(hora, minuto):
    if hora >= 12:
        hora -= 12
        return f'{hora}:{minuto} P.M'
    return f'{hora}:{minuto} A.M'


# Função que define se é par ou ímpar, caso for par retorna True, se não retorna False
def par_impar(numero):
    if numero % 2 == 0:
        return True
    return False

# É conveniente desenvolver os testes em outro módulo separadamente.
