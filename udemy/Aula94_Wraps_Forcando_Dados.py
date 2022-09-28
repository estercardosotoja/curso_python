"""
Wraps e Forcando dados em decoradores
"""

#a) Forçando dados em decoradores
#Ex:
def tipo_dado(*tipos): #Mesma coisa que *args, retorna uma tupla com os elementos
    def decorando(funcao):
        def convertendo_dados(*args,**kwargs):
            #Como args é imutavel devo criar um novo para alterar o tipo das variaveis
            altera_tipo =[]
            altera_tipo.append(tipos[0](args[0]))
            altera_tipo.append(tipos[1](args[1]))
            return funcao(*altera_tipo,**kwargs)
        return convertendo_dados
    return decorando

@tipo_dado(complex,float)
def imprimindo(num1,num2):
    print(f'Numero complexo:{num1} e float:{num2}')

imprimindo('2',2.5)
"""
b)Wraps:
O que faz?
 - Copia os metadados da função antes de ser decorada para sua versão decorada. Portanto, utilizar um decorador não tira a 
   identidade da sua função.
O que são metadados?
 - São dados sobre outros dados Ex: Decorador que é um dado que voce manipula em cima de outro dado(função decorada).

Ex:
Explicando o problema
Nós já vimos o __name__, ele retorna o nome da função a ser usada, enquando o __doc__ retorna justamente a documentação
 daquela função.
Percebemos que ao imprimir a documentação de cont_alunos_aprovados, ele reconhece como a função decorador,
 isso é um problema, pois caso voce tenha um programa e queira consultar a documentação das funções pofissionalmente,
 pode ocorrer conflitos, pois seus metadados estão sobrepostos.
Para consertar esse problema, utilizamos o wraps
Solução:

"""
from functools import wraps


def aprovados(funcao):
    """
     Essa função retorna uma lista completa do nome dos alunos aprovados
    """

    @wraps(funcao)
    def decorador(*args, **kwargs):
        """
        Função que decora e faz os testes de notas
        """
        print(f'{aprovados.__name__}')  # Retornar o nome da função
        print(f'{aprovados.__doc__}')  # Retorna a documentação de aprovados
        aprovado = []
        for chave, nota in kwargs.items():
            if nota >= 6:
                aprovado.append(chave)
        return funcao(*aprovado)

    return decorador


@aprovados
def cont_alunos_aprovados(*args, **kwargs):
    """
    Apresenta a quantidade de alunos aprovados.
    """
    print(f'{cont_alunos_aprovados.__name__}')
    print(f'{cont_alunos_aprovados.__doc__}')
    print(len(args))


cont_alunos_aprovados(Leticia=7, Joao=5, Maria=6, Carlos=8)
