"""
Assertions (Afirmações)
"""
"""
Para que serve?
 - Assertions permitem encontrar bugs rapidamente.
 - Ele irá testar se uma afirmação é verdadeira, caso sim, roda o código, se nao retorna um erro.
 - Pode ser usado no meio dos códigos, sem perdas.
 - Usado para checar tipos de parametros, classes, valores,...
 - São usados mais como complemento dos unittests.
 - Não é recomendavel utilizar o assert como principal teste, pois pode ser desabilitado facilmente com -O que
   para utilizá-lo, basta escrever no terminal python -O nome_do_arquivo.
Modo de declaração:
assert condição
Ex.1:
"""

mensagem = 'Tamo junto'
assert mensagem == 'Tamojunto' #Retorna um erro chamado AssertionError
print(mensagem)

# Ex.2:
# É possível aplicar uma mensagem padrão caso a condição assert seja falsa

mensagem = 'Tamo junto'
assert mensagem == 'Tamojunto', 'Mensagem Incorreta'
print(mensagem)

# Ex.3:

numero = 10j
assert type(numero) is int, 'O numero nao é inteiro'
print(numero)

# Ex.4:


class Teste:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


maria = Teste('Maria')
assert isinstance(maria, Teste)
print(maria.nome)

# Ex.5:


def apaga_arquivos(senha):
    senha_confirma = '123'
    assert senha == senha_confirma
    print('APAGUEI TODOS OS SEUS ARQUIVOS')


apaga_arquivos('12')
