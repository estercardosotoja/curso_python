"""
Pickle e JSON

----------------------PICKLE-----------------------
- O objetivo do Pickle é realizar a serialização ou desserialização dos dados recebidos como objeto.
- Seu conteudo não é entendivel para a leitura humana.
Obs: Apenas faça a leitura de arquivos quando voce tiver certeza se a fonte é confiavel, pois pode conter
conteudo malicioso.

#Escrevendo em arquivos pickle
Ex:
"""

import pickle


class Filme:

    def __init__(self, nome, personagem):
        self.__nome = nome
        self.__personagem = personagem


filme1 = Filme('Senhor dos Aneis', 'Frodo')
filme2 = Filme('Jogos Vorazes', 'Katniss')

with open('Aula111_ManipulandoPickleJson.pickle', 'wb') as arq:
    pickle.dump((filme1, filme2), arq)
    # dump é usado para criar a serialização do conteudo do objeto (Transforma em binario)

# Lendo arquivos pickle
# Ex:

import pickle


class Filme:

    def __init__(self, nome, personagem):
        self.__nome = nome
        self.__personagem = personagem

    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem


filme1 = Filme('Senhor dos Aneis', 'Frodo')
filme2 = Filme('Jogos Vorazes', 'Katniss')

with open('Aula111_ManipulandoPickleJson.pickle', 'wb') as arq:
    pickle.dump((filme1, filme2), arq)
    # dump é usado para criar a serialização do conteudo do objeto (Transforma em binario)

with open('Aula111_ManipulandoPickleJson.pickle', 'rb') as arq:
    filme1, filme2 = pickle.load(arq)
    # Load descarrega o arquivo aplicando a desserialização
    print(f'O filme {filme1.nome} teve como personagem {filme1.personagem}')
    print(f'O filme {filme2.nome} teve como personagem {filme2.personagem}')

"""
-------------------------JSON------------------------
JSON -> JavaScript Object Notation
- Utilizados em API's -> Interface de Programação de aplicativos
https://jsonapi.org/ #Site com exemplos de JSON
Ex.1:
"""


import json


# dumps() -> Faz a formatação para o formato JSON (Aspas duplas)
nome = {'Ana': '30 anos'}
teste_json = json.dumps(nome)
print(teste_json)
print(type(teste_json))

"""
#Em Python, podemos trabalhar com json e pickle juntos, podendo desserializar e serializar objetos.
#Instale: pip install jsonpickle
Ex:
"""

import jsonpickle


class Filme:

    def __init__(self, nome, personagem):
        self.__nome = nome
        self.__personagem = personagem

    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem


"""
filme1 = Filme('Senhor dos Aneis','Frodo')
#print(jsonpickle.encode(filme1)) #encode() é utilizado para criar um dicionario no formato JSON
#O primeiro elemento apresenta qual Classe pertence esse objeto

#Escrevendo arquivos JSONPICKLE:
"""

with open('Aula111_ManipulandoPickleJson.json', 'w') as arq:
    arq.write(jsonpickle.encode(filme1))


"""
    Lendo arquivo JSONPICKLE
    import jsonpickle
"""


class Filme:

    def __init__(self, nome, personagem):
        self.__nome = nome
        self.__personagem = personagem

    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem


filme1 = Filme('Senhor dos Aneis', 'Frodo')

with open('Aula111_ManipulandoPickleJson.json') as arq:
    leitura = jsonpickle.decode(arq.read())
    print(leitura)
    print(leitura.nome)
    print(leitura.personagem)
