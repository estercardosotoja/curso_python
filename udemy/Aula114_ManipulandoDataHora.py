"""
Manipulando Data e Hora
"""
import datetime

# Manipulando somente a hora

jogo = datetime.time(16, 0, 0)
print(jogo)

# Formatar data e hora: strftime()

horarioAtual = datetime.datetime.now()
print(horarioAtual)
horarioAtual_BR = horarioAtual.strftime('%d de %B de %Y')
print(horarioAtual_BR)

# Tabela de formatos do strftime:

#https://docs.python.org/3/library/datetime.html#modulo-datetime

# Dias da semana: weekday()

# 0 - Segunda-feira -> ... -> 6 - Domingo

horarioAtual = datetime.datetime.now()
print(horarioAtual)
print(horarioAtual.weekday())

fimSeculo = datetime.datetime(2100, 12, 31, 23, 59, 59)
print(fimSeculo)
print(fimSeculo.weekday())

# Tempo de execução

import timeit

numQuadrado = str([x ** 2 for x in range(100000)])
print(timeit.timeit(numQuadrado, number=10000))
