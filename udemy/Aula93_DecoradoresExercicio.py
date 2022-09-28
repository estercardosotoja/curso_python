"""
    Faça uma função que calcule a diferença entre dois números, decore-a com outra função adicionando
    as Mensagens: ‘Inicio do Programa’ e ‘Decorando a funcao’. Após isso faça com que o decorador
    permita que apenas seja calculada a diferença positiva entre os dois números, independente
    da ordem de entrada. Imprima o resultado.
"""

def calculo(funcao):
    def decorando(num1, num2):
        return print('Inicio da função\n '
                     'Decorando a funcao')
        if num1 > num2:
            funcao(num1, num2)
        else:
            funcao(num2, num1)
    return decorando

@calculo
def diferenca(num1, num2):
    return num1 - num2


print(diferenca(3, 2))

