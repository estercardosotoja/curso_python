"""
    Crie um programa que leia dois números e mostre a soma entre eles.
"""


num1 = int(input('Digite um valor 1: '))
num2 = int(input('Digite um valor 2: '))
soma = num1 + num2
print(f'A soma desses valores é: {soma}')

"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivéis sobre ele.
"""


algo = input('Digite algo: ')
print(type(algo))

print('Só tem espaços: ', algo.isspace())
print('É um número: ', algo.isnumeric())
print('É alfabético: ', algo.isalpha())
print('É alfanpumerico: ', algo.isalpha())
print('É minusculas :', algo.islower())
print('É maisuculas: ', algo.isupper())
print('Está capitalizada(maiscula e minusculas :', algo.istitle())
