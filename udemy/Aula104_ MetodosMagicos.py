""""""
"""
Métodos Mágicos

- Métodos mágicos são métodos que possuem dunder (__) em seus nomes.

#Exemplos:
__init__ = metódo construtor.
__repr__ = metódo de representação  -> uma representação para a classe.
__str__  = metódo String - semelhante ao objetivo da "__repr__".
__add__  = metódo de Adiconar = é possivel somar ou concatenar dois objetos.
__mul__  = metódo de Multiplicação = É possivel multiplicar dois objetos.
__len__  = metódo que retorna o tamanho.
__del__  = metódo Delete = Deleta o objeto carro, pertindo que informe uma mensagem que foi deletado

"""


class Carro:

    def __init__(self, cor, portas, valor, ano):
        self.cor = cor
        self.portas = portas
        self.valor = valor
        self.ano = ano

    def __repr__(self):
        return f'{self.portas} portas e ano {self.ano}'

    def __str__(self):
        return f'Carro {self.cor} que vale {self.valor}'

    def __add__(self, other):
        return f'{self} ..... {other}'

    def __mul__(self, other):
        if isinstance(other, int): #Valida que o metodo é daquele tipo "isinstance"
            result = ' '
            for i in range(other):
                # 0, 1, 2, 3, 4
                result += ' ' + str(self)
            return result
        return 'É necessário um número inteiro para multiplicar'

    def __len__(self):
        return self.portas

    def __del__(self):
        print('Objeto do tipo Carro deletado!')


carro1 = Carro('prata', 4, 30000, 2011)
carro2 = Carro('vermelho', 2, 130000, 2016)

print(carro1)
print(carro2)
print(carro1 + carro2)
print(carro1 * 5)
print(len(carro1))
print(len(carro2))
print(dir(object))
