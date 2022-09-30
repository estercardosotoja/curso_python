"""
Um time de futsal formado pelo arquivo atletas.csv, que contém nome, altura(cm) e peso(kg) de cada esportista,
deseja fazer uma pesquisa e saber quais atletas tem altura superior a 170 cm e que possui peso menor que
80 kg, imprima o nome deles. Dois reforços entraram para o time no início da temporada, Roberto, 175, 77kg e
Adriana, 165, 60kg. Atualize o arquivo adicionando os jogadores e leia-o novamente.
"""

from csv import *

with open('Aula110_ManipulandoArquivosCSVExercicio_Atletas.csv', encoding='utf-8') as arq:
    leitura = reader(arq, delimiter=',')
    next(leitura)
    for atleta in leitura:
        print(atleta)

    arq.seek(0)
    next(leitura)

    for atleta in leitura:

        if int(atleta[1]) > 170 and int(atleta[2]) < 80:
            print(f'Atletas com alturas maiores que 170 e peso menor que 80: {atleta[0]}')


with open('Aula110_ManipulandoArquivosCSVExercicio_Atletas.csv', 'w', newline='') as arq:
    escrita = writer(arq, delimiter=',')
    escrita.writerow(['Nome', 'Altura', 'Peso'])
    escrita.writerow(['Roberto', '175', '77'])
    escrita.writerow(['Adriana', '165', '60'])


with open('Aula110_ManipulandoArquivosCSVExercicio_Atletas.csv', encoding='utf-8') as arq:
    leitura = reader(arq, delimiter=',')
    next(leitura)
    for atleta in leitura:
        print(atleta)