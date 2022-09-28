"""
Decoradores
"""
"""
O que são Decoradores?
 - São funções que você utiliza para decorar/enfeitar/complementar suas outras funções.

Como declarar?
@nome_da_funcao_decoradora
"""
#Ex:
#Decorar sem utilizar um decorador


def pessoa():
    print('Arthur')


def motivacao(funcao): #Função decoradora
    def decorando():
        funcao()
        print('Continue em frente')
        print('Voce é o melhor')
        print('Carpe diem')
    return decorando


decorada = motivacao(pessoa)
decorada()

#Decorando com o próprio decorador


def motivacao(funcao): #Função decoradora
    def decorando():
        funcao()
        print('Continue em frente')
        print('Voce é o melhor')
        print('Carpe diem')
    return decorando


#Para utilizar a funcao decoradora, devemos declara-la antes de usar o decorador
@motivacao #Decorador
def pessoa():
    print('Arthur')


pessoa() #Utilizando o decorador basta eu executar a função decorada que já estará funcionando.


#Isso é a mesma coisa que isso:
def motivacao(): #Função decoradora
    def decorando():
        print('Continue em frente')
        print('Voce é o melhor')
        print('Carpe diem')
    return decorando

def pessoa():
    print('Arthur')
    decorada = motivacao()
    decorada()

pessoa()

                  #OU


def motivacao():
    print('Continue em frente')
    print('Voce é o melhor')
    print('Carpe diem')


def pessoa():
    print('Arthur')
    motivacao()


pessoa()

#Qual a vantagem?
#- Usando decoradores voce tem o trabalho de criar a funcao decoradora apenas uma vez e basta chamá-la com @
#- Melhor visualização caso ocorra um erro.
#- São comuns em frameworks web(desenvolvimento de sites) como Flask e Bottle.

#Passando parâmetros nos decoradores:
#Ex:


def calculadora(funcao):
    def decorando(x,y,op):
        print(f'Farei a operacao soma de {x} e {y}')
        return funcao(x,y,op)
    return decorando

@calculadora
def soma(num1,num2,op):
    return num1 + num2


print(soma(2,5,1))

#Mas e se o numero de parametros de entrada for diferente???
#Programa com problema:


def calculadora(funcao):
    def decorando(x,y,z,op): #Os parametros dependem de qual funcao o usuario deseja decorar
        if op == 1:
            print(f'Farei a operacao soma de {x} e {y}')
            return funcao(x,y,op)
        else:
            print(f'Farei a operacao multiplicacao de {x}, {y} e {z}')
            return funcao(x, y, z, op)
    return decorando


@calculadora
def soma(num1,num2,op):
    return num1 + num2


@calculadora
def mul(num1,num2,num3,op):
    return num1 * num2 * num3


print(soma(2,5,1))
print(mul(2,3,3,2))

#Qual a solução?? Basta utilizar *args e **kwargs
#Lembrando: args retorna uma tupla(imutavel) e kwargs retorna um dicionario(chave -> dado)
#Solução: Programa correto


def calculadora(funcao):
    def decorando(*args,**kwargs):
        if len(args) == 2:
            print(f'Farei a operacao soma de {args[0]} e {args[1]}')
            return funcao(*args,*kwargs)
        else:
            print(f'Farei a operacao multiplicacao de {args[0]}, {args[1]} e {args[2]}')
            return funcao(*args,*kwargs)
    return decorando


@calculadora
def soma(num1,num2):
    return num1 + num2


@calculadora
def mul(num1,num2,num3):
    return num1 * num2 * num3


print(soma(2,5))
print(mul(2,3,3))


#Dica extra: Forçar parametros com decorador
#Ex:
#Forçando para o primeiro numero dado na operação deve ser o requisitado pelo programador


def obrigando_primeiro_valor(numero):
    def calculadora(funcao):
        def decorando(*args, **kwargs):
            if args[0] == numero:
                if len(args) == 2:
                    print(f'Farei a operacao soma de {args[0]} e {args[1]}')
                    return funcao(*args,*kwargs)
                else:
                    print(f'Farei a operacao multiplicacao de {args[0]}, {args[1]} e {args[2]}')
                    return funcao(*args,*kwargs)
            else:
                return f'O primeiro valor deve ser {numero}'
        return decorando
    return calculadora


@obrigando_primeiro_valor(3)
def soma(num1,num2):
    return num1 + num2


@obrigando_primeiro_valor(3)
def mul(num1,num2,num3):
    return num1 * num2 * num3


print(soma(3,5))
print(mul(3,3,3))
