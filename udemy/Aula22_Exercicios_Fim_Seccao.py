"""
1) Faça uma função que receba um número inteiro maior que zero e retorne a soma de todos os algarismos.
Caso o valor seja negativo retorne 'Numero inválido'
Exemplo:
251 = 2 + 5 + 1 = 8
"""


def entrada():
    valor = int(input("Digite o valor que deseja: "))
    if valor >= 0:
        soma(valor)
    else:
        return "Número Inválido!"


def soma(valor):
    

entrada()
