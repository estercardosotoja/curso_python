"""

1 - Realizar a media das notas 4 alunos.

2 - Converter uma temperatura de graus 'C para 'F e para K.
Dados: 'F = 'C * 1.8 + 32
        K = 'C + 273.15

"""
#Problema 1
num1 = int(input('Digite a nota do aluno 1: '))
num2 = int(input('Digite a nota do aluno 2: '))
num3 = int(input('Digite a nota do aluno 3: '))
num4 = int(input('Digite a nota do aluno 4: '))

media = ((num1 + num2 + num3 + num4) / 4)

print(f'Média das notas {media}')

#Problema 2
celsius = input('Digte a temperatura em Graus Celsius:')
Faren = (int(celsius) * 1.8) + 32
print(f'A temperatura em Fahrenheit °F: {Faren}')
kelvin = int(celsius) + 273.15
print(f'A temperatura em Fahrenheit °F: {kelvin}')

