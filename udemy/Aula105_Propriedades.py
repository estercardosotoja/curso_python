"""
Propriedades

- Métodos públicos utilizados para manipular atributos/métodos privados.
  Em Java usamos o get e o set, em Python usamos as Propriedades

#Exemplos
"""


class Celular:

    def __init__(self, data, senha, saldo_banco, msg):
        self.__data = data
        self.__senha = senha
        self.__saldoBanco = saldo_banco
        self.__msg = msg

    @property
    def data(self):
        return f'Data de hoje: {self.__data}'

    @property
    def senha(self):
        return self.__senha

    @property
    def saldo_Banco(self):
        return self.__saldoBanco

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, resposta):
        self.__msg = resposta

    @property
    def mensagem(self):
        return f'Data: {self.__data}. Mensagem: {self.__msg}'


cel1 = Celular('18/11/2024', 'Mortadela1', 3210, 'Ei, sumido(a)!')
cel2 = Celular('10/03/2023', 'Ab4caxi', 4210, 'Tirou a carne do congelador?')

print(cel1.data)

print(cel1.senha)

print(f'Saldo total: {cel1.saldoBanco + cel2.saldoBanco}')

print(cel1.msg)
cel1.msg = 'Olá, como vai?'
print(cel1.msg)

print(cel2.msg)
cel2.msg = 'Esqueci!! :('
print(cel2.msg)

# Método como propriedade


print(cel1.mensagem)
print(cel2.mensagem)
