"""
Leitura e Escrita - Arquivo CSV

CSV -> Comma Separated Values (Valores Separados por Virgula)
Ex:
1,2,3,4,5,6
1:2:3:4:5:6
1;2;3;4;5;6
1 2 3 4 5 6
Dentre outros...

Ex:
http://dados.gov.br/dataset

#Abrindo arquivo csv para leitura(Modo Não Pythonico):
"""

print('\n \n ---------------- Exercicio1 -----------------')
with open('Aula110_ManipulandoArquivosCSV_Pessoas_Famosas.csv') as arq:
    informacoes = arq.readlines()
    # Le linha por linha
    print(type(informacoes))
    # Lista
    print(informacoes)
    # Cada indice da lista representa uma linha
    for elemento in informacoes:
        print(elemento, end='')
    del informacoes[0]
    # Deleta o cabeçalho
    print(informacoes)
    for indice, conteudo in enumerate(informacoes):
        print(indice)
        # Retornar o indice
        print(conteudo)
        # Retorna o conteudo
        informacoes[indice] = conteudo.split(',')
    print(informacoes)

"""
-------------------------Leitura--------------------------
Abrindo arquivo csv para leitura(Modo Pythonico)
a)Reader() -> Itera as linhas do arquivo como lista.
Ex:

"""

from csv import reader

print('\n \n ---------------- Exercicio2 -----------------')
with open('Aula110_ManipulandoArquivosCSV_Pessoas_Famosas.csv', encoding='utf-8') as arq:
    # encoding='utf-8' = aceita acentos, padrão de leitura de arquivos
    leitura = reader(arq, delimiter=',')
    print(type(leitura))
    next(leitura)
    # Retira o cabeçalho
    for teste in leitura:
        print(teste)
    arq.seek(0)
    # retorna para o inicio do arquivo
    next(leitura)
    for linha in leitura:
        print(f'{linha[0]} participou do filme {linha[1]}')

"""
OBS: Caso apresente erro de leitura por caracteres especiais faça:
open('pessoas_famosas.csv',encoding='utf-8')
Caso há outro separador, como ; : / etc faça:
leitura = reader(arq,delimiter = '/')

b)DictReader():
 ->Itera as linhas do arquivo csv como dicionarios.
Ex:
"""
from csv import DictReader


print('\n \n ---------------- Exercicio3 -----------------')
with open('Aula110_ManipulandoArquivosCSV_Pessoas_Famosas.csv') as arq:
    leitura = DictReader(arq)
    print(leitura)
    for teste in leitura:
        print(teste)
    arq.seek(0)
    next(leitura)
    for linha in leitura:
        print(f"{linha['Pessoa']} participou do filme {linha['Filme']} ")

"""
----------------------Escrita----------------------
a)Writer(): Permite a escrita em csv usando listas
Obs: writerow() ->Para escrever cada uma das linhas, sendo que recebe como parametro listas.
Ex:

"""
from csv import writer


print('\n \n ---------------- Exercicio4 -----------------')
with open('Aula110_ManipulandoAquivosCSV_Animais.csv', 'w', newline='') as arq:
    # OBS: Newline é usado para não pular linha no arquivo em alguns Sistemas Operacionais
    escrita = writer(arq, delimiter=':')
    escrita.writerow(['Animal', 'Tipo'])
    for numero in range(0, 2):
        animal = input('Digite o nome do animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow([animal, tipo])

"""
b)DictWriter(): Permite a escrita em csv, mas utilizando dicionarios
Ex:

"""
from csv import DictWriter


print('\n \n ---------------- Exercicio5 -----------------')
with open('Aula110_ManipulandoAquivosCSV_Animais.csv', 'w', newline='') as arq:
    titulos = ('Animal', 'Tipo')
    escrita = DictWriter(arq, delimiter='/', fieldnames=titulos)
    escrita.writeheader()
    # Serve para adicionar os titulos como primeira linha
    for item in range(2):
        animal = input('Digite o nome do animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow({'Animal': animal, 'Tipo': tipo})
        # A nomeclatura das chaves devem ser identicas ao que tem nos titulos
