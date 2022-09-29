"""
1) Crie uma classe chamada Personagem que irá receber como construtor o
nome completo, altura, peso e resistência (0-100) do personagem, além disso,
também crie um método que se chame poder que conterá todos os atributos de
instancia como privado não sendo possível alterá-los, sendo estes: magia,
persuasão, agilidade e forca, cada um avaliada de 0 a 100, por fim, retorne
apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
imprima o nome completo e quantidade de poder total do mais forte.

"""


class Personagem:

    def __init__(self, nome, alt, peso, resis):
        self.nome = nome
        self.alt = alt
        self.peso = peso
        self.resis = resis

    def poderes(self, magia, persuasao, agilidade, forca):
        self.__magia = magia,
        self.__persuasao = persuasao,
        self.__agilidade = agilidade,
        self.__forca = forca

        return magia + forca + agilidade + persuasao


dict_poder = {}

rainha_ma = Personagem("Rainha Má", 1.60, 80.6, 50)
dict_poder[rainha_ma.nome] = rainha_ma.poderes(90, 80, 60, 20)
super_homem = Personagem("Super-Homem", 1.90, 95.6, 98)
dict_poder[super_homem.nome] = super_homem.poderes(20, 40, 70, 99)
bob_esponja = Personagem("Bob Esponja", 0.90, 5, 50)
dict_poder[bob_esponja.nome] = bob_esponja.poderes(30, 80, 90, 30)

maior_poder = 0
nome_poder = ''

for chave,valor in dict_poder.items(): #A Ferramenta items() retorna
    if maior_poder < valor:
        maior_poder = valor
        nome_poder = chave
print(f'O mais personagem mais forte eh: {nome_poder} \n'
      f'E possui o total de: {maior_poder} pontos de poder')
