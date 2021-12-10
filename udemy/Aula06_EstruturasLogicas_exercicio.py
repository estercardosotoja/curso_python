"""
1 - Cire um sistema de cadastro o login de um site, utilizando um username e senha informados pelo usuário.
"""

username = 'Ester'
senha = 1234
print("------------------  Bem Vindo  ----------------")
print("------------------  Faça seu login  ----------------")
usernameDigitado = input("Digite seu username: ")
senhaDigitada = int(input("Digite sua senha: "))

if (usernameDigitado == username) and (senhaDigitada == senha):
    print("-------- Login Realizado com sucesso  :) --------")
elif (usernameDigitado != username) or (senhaDigitada == senha):
    print("-------- Username Invalido  --------")
elif (usernameDigitado == username) or (senhaDigitada != senha):
    print("-------- Senha Invalido  --------")
else:
    print("-------- Username e Senha invalidos :(  --------")

"""
2 - Crie um programa e encontre e imprima as raizes  de um equação do segundo grau,
utilizando o metódo de Bhaskara

# Equação de 2°  =  A * x ** 2 + B * x + C
"""

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c) #Encontra o delta
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

#Na matemática a raiz quadrada de um npumero é igual a este numero elevado á meio (0.5)

print(f'As raizes são: {x1} e {x2}')

# Outro modo de ser realizada a potencia é utilizando o modulo math:
# import math
# x1 = (-b + math.sqrt(delta)) / (2 * a)
