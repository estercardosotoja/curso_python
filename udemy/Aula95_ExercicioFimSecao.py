"""
Exercicio de Seção
"""
"""
Decorar o exercício da Aula de Nested Functions e executar as três funções.
- Na função que executa a string maiúscula use um decorador para imprimir: ’Estou gritando’.
- Na função que soma dois números decore com ‘O maior entre os dois é: {maior}’.
- Na função que soma um número com outro aleatório decore com ‘Somando com o aleatório:'
- Faça o tratamento com Wraps do programa.
A seguir está apresentado o problema sem decoração (Podem retirar os comentários caso seja necessário):

"""

"""
    Crie uma função que contenha 3 funções dentro:
    - Uma delas deixa a string toda maiúscula.
    - Outra que Soma dois números passados pelo usuário.
    - E, a ultima soma um numero passado pelo usuário com um numero aleatório entre 0 e 15 com o comando
     randint().
"""

from random import randint
from functools import wraps

def decorando_funcoes(funcao): #Função decoradora
    @wraps(funcao)
    def interna(*args,**kwargs):
        #Decorando upper_str
        if args[0] == 'upper_str':
            print('Estou Gritando')
        #Decorando soma
        elif args[0] == 'soma':
            if args[1] > args[2]:
                print(f'O maior entre os dois é: {args[1]}')
            else:
                print(f'O maior entre os dois é: {args[2]}')
        #Decorando soma_maluca
        elif args[0] == 'soma_maluca':
            print('Somando com o aleatório: ')
        return funcao(*args,**kwargs)
    return interna

@decorando_funcoes #Decorador
def funcao_externa(*args): #args recebera os parametros em forma de
                           #tupla
    if args[0] == 'upper_str': #Se o primeiro indice possui esse nome
                               #faça:
        def upper_str():
            try: #Tente:
                print(args[1].upper()) #Imprima a string maiuscula
            except AttributeError: #Caso o usuario mande um numero
                                   #faça:
                print('Nao tem como aplicar upper() em variaveis que nao sejam str')
        return upper_str #Retorna a função
    elif args[0] == 'soma': #Se não se o primeiro indice possui esse
                            #nome faça:
        def soma():
            try:
                print(f'Soma: {args[1] + args[2]}')
            except TypeError: #Caso o usuario passe letras
                print('Deve conter apenas numeros')
            except IndexError: #Caso o usuario passe menos parametros
                               #desejados
                print('Deve passar dois numeros como parametro')
        return soma
    elif args[0] == 'soma_maluca': #Se não se o primeiro indice possui
                                   #esse nome faça:
        def soma_maluca():
            try:
                print(f'{args[1]+randint(0,15)}')
            except TypeError: #Caso o usuario passe uma string
                print('Deve-se conter apenas numeros')
        return soma_maluca
    else: #Condição para nenhuma função chamada
        def erro():
            print('Nenhuma funcao chamada')
        return erro


#Seguindo o enunciado, o primeiro elemento deve ser o nome da função que deseja e o restante de acordo com a função
resposta = funcao_externa('soma_maluca', 1) #Armazena o objeto função
                                           #dentro de resposta
resposta() #Executa a função de fato e retorna 1 + inteiro aleatorio
resposta = funcao_externa('soma', 1, 2)
resposta() #Retorna Soma:3
resposta = funcao_externa('upper_str', 'teste')
resposta() #Retorna TESTE
resposta = funcao_externa('oi', 'teste')
resposta() #Retorna nenhuma função chamada
