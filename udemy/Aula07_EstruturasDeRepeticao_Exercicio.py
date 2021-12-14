"""
1) Faça um programa que calcule a soma de divisores de um um número inteiro definindo pelo usuário.
EX: Se o usuário escolheu 10, temos =  1 + 2 + 5 + 10 = 18
"""

soma = 0
num = int(input('Digite um numero: '))

for numero in range(1, num + 1):
   if num % numero == 0:
        soma = soma + numero
print(soma)

"""
2) Faça um programa que imprima os n primeiros multplos  de 5, sendo n definido pelo usuario .
   Se o usuario escolheu n = 3 , será impresso 5, 10, 15.
   Solução: 
"""

num = int(input("Digite o numero: "))
multi = 0

intervalo = range(1, num+1)
for num in intervalo:
    multi = 5 + multi
    print(multi)
