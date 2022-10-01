"""
Exercícios:
1) Aplique assert’s no código abaixo e descreva o que o programa faz:
"""


class ContaCorrente:

    def __init__(self, nome, num_conta, saldo=0.0):
        self.__nome = nome
        self.__num_conta = num_conta
        self.__saldo = saldo
        assert type(nome) is str, 'O atributo nome deve ser do tipo string'
        assert type(num_conta) is int, 'O atributo num_conta deve ser do tipo inteiro'
        assert type(saldo) is float, 'O atributo saldo deve ser do tipo float'
        assert saldo >= 0, 'O saldo não pode ser negativo'

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def num_conta(self):
        return self.__num_conta

    def deposito(self, valor):
        assert valor > 0, 'O atributo valor deve ser positivo'
        assert valor is float, 'O atributo valor deve ser do tipo float'
        self.__saldo = self.__saldo + valor

    def saque(self, valor):
        assert valor > 0, 'O atributo valor deve ser positivo'
        assert valor is float, 'O atributo valor deve ser do tipo float'
        assert self.saldo >= valor, 'O atributo saldo deve ser maior ou igual ao atributo valor'
        self.__saldo = self.__saldo - valor


pessoa = ContaCorrente('Sandro', 12345)
pessoa2 = ContaCorrente('Vanessa', 67891, 500.0)
