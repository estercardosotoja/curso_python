'''
1 - Crie um arquivo de texto na pasta onde está seu programa Python. O
    arquivo deve conter alguns números de 4 dígitos separados por linha,
    representando números de uma rifa. Após isso, itere no arquivo para colocar os
    valores em uma lista. Por fim, utilize a função choice() para determinar o
    ganhador.
'''
from random import choice as ch

rifaNum = []

with open('Aula84_LerArquivoExercicio.txt') as file:
    for num in file:
        rifaNum.append(int(num))

print("O numero sorteado é: ", ch(rifaNum))



