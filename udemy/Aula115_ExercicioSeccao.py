"""
1 - Dudu é um famosinho do instagram e precisa manter postagens em seu
feed regularmente. Portanto teve a ideia de criar um programa em Python que
agende suas publicações para todas segundas, quartas e sextas ao longo de
um mês, a partir deste momento. Além disso, seus posts irão variar entre os
temas: saúde, vida pessoal e motivacional. Com isso, utilize choice() para
selecionar cada conteúdo aleatoriamente. Faça um programa que implemente
a ideia de Dudu, imprimindo o conteúdo de cada um dos dias e seus
respectivos dias de postagem
"""
import datetime
from random import choice as ch

Temas = ['Saúde', 'Vida pessoal', 'Motivacional']

esteMomento = datetime.datetime.now()
print(esteMomento)
print(repr(esteMomento))

mesqvem = esteMomento + datetime.timedelta(30)
print(mesqvem)
print(repr(mesqvem))
print('\n')

while (esteMomento.day <= mesqvem.day) or (esteMomento.month < mesqvem.month):
    if esteMomento.weekday() == 0:
        print(f'Segunda-feira, {esteMomento}. Tema: {ch(Temas)}')
    elif esteMomento.weekday() == 2:
        print(f'Quarta-feira, {esteMomento}. Tema: {ch(Temas)}')
    elif esteMomento.weekday() == 4:
        print(f'Sexta-feira, {esteMomento}. Tema: {ch(Temas)}')
        esteMomento += datetime.timedelta(1)
