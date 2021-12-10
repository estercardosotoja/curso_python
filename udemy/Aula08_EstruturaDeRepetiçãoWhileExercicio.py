"""

1) Faça um programa que calcule o maior palindromo resultado do produto de dois números de 3 digitos.
Polindromo são numeros que lendo da esquerda para a direita resulta no mesmo caso leia da direita para a esquerda.
EX: 52625
EX: O maior políndromo resultado do produto de dois números é 91*99 = 9009

"""

n1 = 9999
res = 0

while n1 != 0:
    n2 = n1
    while n2 != 0:
        numero = str(n1 * n2)
        inverte_numero = numero[::-1]
        if inverte_numero == numero:
            num = int(numero)
            if res < num:
                res = num
                n2 -= 1
            else:
                n2 -= 1
        else:
            n2 -= 1
    n1 -= 1

print(res)

"""
Media dos 5 primeiros números primos da Sequência Fiabinacci
"""

ant1 = 0
pro = 1
parada = 1

while parada <= 5:
    print(pro)
    pro = pro + ant1
    ant1 = pro - ant1
    parada = parada + 1
print('fim')

"""
Media dos 5 primeiros números primos da Sequência Fiabinacci apresentando somente o números primos
"""

ant2 = 0
pro2 = 1
parada2 = 1

while parada2 <= 5:
     print(pro2)
     pro2 = pro2 + ant2
     ant2 = pro2 - ant2
     parada2 = parada2 + 1
     divisor = 1
     num_div_int = 0
     while divisor <= pro:
        if pro % divisor == 0:
            num_div_int += 1
        divisor += 1
     if num_div_int == 2:
         soma = soma + pro
         print(pro)
         parada += 1
print(soma / 5)
