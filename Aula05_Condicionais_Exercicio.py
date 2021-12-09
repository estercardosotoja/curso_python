"""

1 - Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potencia)
Peça a operação desejada e depois os dois numeros ao usuário.

"""

num1 = float(input(f'Digite o primeiro numero: '))
num2 = float(input(f'Digite o segundo numero: '))
operacao = int(input(f'Digite qual a operação desejada: '
                     f' 1 - Soma:'
                     f' 2 - Multiplicação:'
                     f' 3 - Divisão Inteira:'
                     f' 4 - Potencia: '))

if operacao == 1:
    soma = num1 + num2
    print(f' O resultado da soma é: {soma}')
elif operacao == 2:
    multi = num1 * num2
    print(f' O resultado da multiplicação é: {multi}')
elif operacao == 3:
    divi_inteiro = num1 // num2
    print(f' O resultado da divisão por inteiro é: {divi_inteiro}')
elif operacao == 4:
    potencia = num1 ** num2
    print(f' O resultado da potencia é: {potencia}')
else:
    print('Operacao Invalida!')
