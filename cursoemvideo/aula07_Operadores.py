"""
"Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor"
"""

num = int(input('Digite um numero: '))
print(f' O antecessor: {num - 1} \n O numero escolhido: {num}  \n O Sucessor: {num + 1}')

"""
Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada.
"""

num = int(input('Digite um numero: '))
print(f' O dobro: {num * 2} \n O seu triplo {num * 3} \n E a raiz quadrada {num ** 1.5}')

"""
Desenvolva um programa que leia duas notas de um aluno e calcule e mostre a sua média
"""

nota1 = int(input('Digite sua nota 1: '))
nota2 = int(input('Digite sua nota 2: '))
media = (nota1 + nota2)/2
print(f"Sua média é: {media}")

"""
Escreva um programa que leia um valor em metros e o exiba convetido em centimetros e milimetros.
1 metro  = 100 centimetros
1 centimentro = 10 milimetros
"""

metro = int(input('Digite um valor em metros: '))
print(f'\n Metros: {metro} \nCentimetro: {metro * 100} \nMilimetros: {(metro * 100) * 10}')

"""
Faça um programa que leia um número inteiro qualquer e mostre na sua tela a sua tabuada
"""

num = int(input('Digite um numero: '))
print(f'Tabuada do número: {num}'
      f'\n 0 x {num} = {num * 0}'
      f'\n 1 x {num} = {num * 1}'
      f'\n 2 x {num} = {num * 2}'
      f'\n 3 x {num} = {num * 3}'
      f'\n 4 x {num} = {num * 4}'
      f'\n 5 x {num} = {num * 5}'
      f'\n 6 x {num} = {num * 6}'
      f'\n 7 x {num} = {num * 7}'
      f'\n 8 x {num} = {num * 8}'
      f'\n 9 x {num} = {num * 9}'
      f'\n 10 x {num} = {num * 10}')

"""
Faça um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
Considere: US$ 1.00 = R$3.27
"""

reais = float(input('Digite um valor em reais: R$'))
print(f'Pode comprar: UR$ {reais / 3.27:.2f} doláres')

"""
Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta pinta uma área quadrada de 2m^2
"""

larg = float(input('Digite a largura em metros: '))
alt = float(input('Digite a altura em metros: '))
area = larg * alt
litro = (area) / 2
print(f"O tamanho da área: {area:.2f} \nO valor em litros de tinta: {litro:.2f}")

"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = float(input('Digite o preco do produto: '))
print(f'O 5% de desconto = {((preco*5)/100)-preco:.2f}')

"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Digite o valor do salario: '))
print(f'O 5% de desconto = {((salario*15)/100)+salario:.2f}')


"""
Escreva um programa que converta uma temperatura, digitando em graus Celsius e converta para graus Fahrenheit.
"""

cel = float(input('Digite a temperatura: '))
print(f'A temperatura em Celsius = {cel}°C '
      f'\nA temperatura em Kelvin = {cel + 273.15:.2f} '
      f'\nA temperatura em Fahrenghti = {cel + 32:.2f}F')

"""
Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R60,00 por dia e R$0,15 por KM rodado.
"""

km = float(input('Digite o KM percorrido: '))
dias = int(input('Digite a quantidade de dias do carro que foi alugado: '))

alugado = dias * 60.00
valor_km = km * 0.15
print(f'O valor pela diaria= {alugado} \nO valor pela kilometragem= {valor_km} \nO valor total = {alugado + valor_km}')
