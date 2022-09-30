""""""
"""
Herança

- Aumentar o alcance de nossas classes utilizando menos código.
- Se uma classe herda de outra classe, ela passa a herdar todos os atributos e métodos da classe
herdada.

A classe herdada é conhecida como:
    Classe Mãe
    Classe Pai
    Classe Base
    Classe Genérica
    Super Classe

A classe que herda é conhecida como:
    Classe Filha
    Classe Específica
    Sub Classe
"""


class Aparelho:

    def __init__(self, marca, peso, volume):
        self.__marca = marca
        self.__peso = peso
        self.__volume = volume

    def volume(self):
        return f'O volume está em {self.__volume}'


class Televisao(Aparelho):

    def __init__(self, marca, peso, volume, polegadas):
        super().__init__(marca, peso, volume)
        self.__polegadas = polegadas

    def volume(self):
        print(super().volume())
        return f'Olha só, {super().volume()}'


class Radio(Aparelho):

    def __init__(self, marca, peso, volume, frequencia):
        super().__init__(marca, peso, volume)
        self.__frequencia = frequencia


tv = Televisao('LG', 2.5, 80, 52)
radio = Radio('Sony', 1, 75, 105)

print(tv.volume())
print(radio.volume())

#Método super() pode acessar qualquer atributo e método da Super Classe.

#Overriding: Reescrever um método presente na Super Classe em uma Sub Classe.