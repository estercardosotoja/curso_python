"""
    1) Crie dois arquivos: um CSV e um JSONPICKLE. Escreva os lucros de uma
    empresa em um balanço trimestral, apresentando o mês e o lucro em milhões
    no CSV, e as despesas nos mesmos meses em JSONPICKLE a partir dos
    objetos criados com uma classe chamada Empresa. Após isso, troque seus
    conteúdos, ou seja, armazene os valores dos lucros no JSONPICKLE e os
    valores de despesa no CSV.
"""
from _csv import writer, reader

import jsonpickle


class Empresa:

    def __init__(self, mes, dinheiro):
        self.__mes = mes
        self.__dinheiro = dinheiro

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, novo_dinheiro):
        self.__dinheiro = novo_dinheiro


janeiro = Empresa('Janeiro', 4)
fevereiro = Empresa('Fevereiro', 6)
marco = Empresa('Marco', 7)


with open('lucros.csv', 'w', newline='') as arq:
    escrita = writer(arq, delimiter=':')
    escrita.writerow(['Mes', 'Dinheiro(Milhoes)'])
    escrita.writerow(['Janeiro', '10'])
    escrita.writerow(['Fevereiro', '3'])
    escrita.writerow(['Marco', '11'])

list = []
list.append(janeiro)
list.append(fevereiro)
list.append(marco)

with open('despesas.json', 'w') as arq:
    arq.write(jsonpickle.encode(list))

despesas = []
lucros = []


with open('lucros.csv') as arq_csv:
    with open('despesas.json') as arq_jsonpickle:

        list = jsonpickle.decode(arq_jsonpickle.read())
        janeiro = list[0]
        fevereiro = list[1]
        marco = list[2]

        despesas.append(janeiro.dinheiro)
        despesas.append(fevereiro.dinheiro)
        despesas.append(marco.dinheiro)

        leitura = reader(arq_csv, delimiter=':')
        next(leitura)
        for linha in leitura:
            lucros.append(linha[1])

with open('lucros.csv', 'w', newline='') as arq_csv:
        escrita = writer(arq_csv)
        escrita.writerow(['Mes', 'Dinheiro(Milhoes)'])
        escrita.writerow(['Janeiro', despesas[0]])
        escrita.writerow(['Fevereiro', despesas[1]])
        escrita.writerow(['Marco', despesas[2]])


with open('despesas.json', 'w') as arq_jsonpickle:
    janeiro.dinheiro = lucros[0]
    fevereiro.dinheiro = lucros[1]
    marco.dinheiro = lucros[2]
    list = []
    list.append(janeiro)
    list.append(fevereiro)
    list.append(marco)
    arq_jsonpickle.write(jsonpickle.encode(list))
