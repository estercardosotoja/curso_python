"""
1 - Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome
como parâmetro. Estas classes devem herdar de outras duas chamadas
'Carnivoros' e 'Herbivoros', que possuem dois métodos cada ('caçar_animal' e
'comer_carne' para 'Carnivoros', 'procurar_arvore' e 'comer_folhas' para
'Herbivoros') e herdam de uma Superclasse chamada 'Animal', na qual possui
os métodos 'andar' e 'correr'. Por fim, instancie dois objetos, da classe 'Homem'
e da classe 'Urso', e execute todos os métodos.
Obs.: Crie um método para as classes 'Homem' e 'Urso' representando uma
ação característica de cada, por exemplo ler um livro para o homem e hibernar
para o urso
"""


class Animal:

    def andar(self):
        print('Andar')

    def correr(self):
        print('Correr')


class Carnivoros(Animal):

    def cacar_animal(self):
        print('Caçando..')

    def comer_carne(self):
        print('Comendo..')


class Herbivoros(Animal):

    def procurar_arvore(self):
        print('Procurando em árvores..')

    def comer_folhas(self):
        print('Comendoa as nas árvores..')


class Homem(Carnivoros, Herbivoros):

    def __init__(self, nome):
        self.nome = nome

    def ler(self):
        print('Lendo..')

    def escrevendo(self):
        print("Escrevendo")


class Urso(Carnivoros, Herbivoros):

    def __init__(self, apelido):
        self.apelido = apelido

    def hibernar(self):
        print('Hipernando..')

    def brincando(self):
        print('Nadando..')


buf = Urso('Buff')
jorge = Homem('Jorge')

print("--- Humano ---")
jorge.ler()
jorge.andar()
jorge.comer_folhas()
jorge.comer_carne()

print("\n \n m--- Urso ---")
buf.andar()
buf.hibernar()
buf.procurar_arvore()
buf.correr()
buf.cacar_animal()
buf.comer_carne()
