"""
    Crie uma função que contenha 3 funções dentro:
    - Uma delas deixa a string toda maiúscula.
    - Outra que Soma dois números passados pelo usuário.
    - E, a ultima soma um numero passado pelo usuário com um numero aleatório entre 0 e 15 com o comando
     randint().
"""
from random import randint


def maiuscula(palavra):
    return palavra.upper()


def soma(num1, num2):
    return num1 + num2


def num_aleatorio():
    return randint(0, 15)


def soma_valores():
    num_user = int(input("Digite um valor: \n"))
    return soma(num_user, num_aleatorio())


print(soma_valores())
