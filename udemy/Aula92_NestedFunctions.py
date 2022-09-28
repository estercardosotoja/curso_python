"""
Nested Functions
"""

#Nested functions = Funções dentro de funções
#a) Criar uma variavel do tipo função:
#Ex:
def aniversariantes(lista_nomes):
    for nome in lista_nomes:
        print(f'Feliz aniversario {nome}')

felicitacoes = aniversariantes #Não utilize () pois assim voce estará executando a função
felicitacoes(['Lucas','Vitoria'])
print(type(felicitacoes)) #Retorna um tipo função
print(felicitacoes) #Retorna a função aniversariantes em um endereço especifico de memória

#b) Passando funções como argumento/parametro:
#Ex:
from random import randint

def num_aleatorio():
    return randint(1,6)

def pessoa(funcao,nome):
    resultado = funcao()
    if resultado < 4:
        return str(resultado) + ',Finish,' + nome
    else:
        return str(resultado) + ',Vitoria Perfeita,' + nome

print(num_aleatorio()) #Executando a função num_aleatorio
print(num_aleatorio) #Estou passando o nome da função apenas
print(pessoa(num_aleatorio,'Vanessa')) #Não quero passar a execução, mas sim o nome da função, para isso não utilizo ()

#c) Retornando uma função dentro de função:
#Ex.1:
from random import randint

def pessoa(nome):
    def num_aleatorio():
        return randint(1, 6)
    return f'{nome} tirou {num_aleatorio()}' #Retorna a execução de num_aleatorio

print(pessoa('Claudio'))
#Obs:
#print(num_aleatorio()) #Dará NameError pois quando uma função está dentro de outra, ela não é reconhecida externamente.

#Ex.2:
from random import randint

def pessoa():
    def num_aleatorio():
        return randint(1,6)
    return num_aleatorio

print(pessoa()) #Imprime a função num_aleatorio em si
funcao = pessoa()
print(funcao()) #Permite acessar funções internas com esse método

#d) Parametros passados para funções externas são reconhecidos em funções internas:
#Ex:
from random import randint

def pessoa(nome):
    def num_aleatorio():
        return f'{nome} tirou {randint(1,6)}'
    return num_aleatorio

funcao = pessoa('Davila')
print(funcao()) #Imprime o nome mesmo nao sendo passado como parametro para num_aleatorio
