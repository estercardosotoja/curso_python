"""

* args e **kwargs

- São parâmetros como quaisquer outros
- Não são obrigatórios (não exigem argumentos)
- Seus nomes não importam, e sim o(s) asterisco(s). # *batata, **bode
- Os nomes args e kwargs são apenas por convenção
- Ajudam a evitar erros e tornam a função mais dinâmica
"""
# *args
# *args armazena os argumentos EXTRAS em uma tupla.

# Exemplo 1
def cadastro(nome, idade, *args):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(args)
    print(f'Profissão: ', end=' ')
    for prof in args:
        print(prof, end=' ')

cadastro('Agnaldo', 87, 'carpinteiro', 'lutador', 'garçom')

#Exemplo 2
def media(peixe, num2, *args):
    print(args)
    print(sum(args)/len(args))

media(1, 2, 3, 4, 5)

# Exemplo 3 - *args com coleção de dados
notas = [8, 9.7, 2.3, 5, 10, 0, 0, 2, 6.9]

def somarNotas(*args):
    print(args)
    print(sum(args))

#somarNotas(notas) #TypeError Dessa forma encaminha toda a dupla como um objeto apenas
somarNotas(*notas) #Dessa forma envia cada elemento para a função.
#somarNotas()

# Obs.: O asterisco no argumento informa que deve haver um desempacotamento da coleção de dados
#(listas, tuplas, conjuntos), antes que a mesma seja enviada para a função

# **kwargs
# **kwargs armazena os argumentos EXTRAS E NOMEADOS em um dicionário.

# Exemplo 1
def idades(**kwargs):
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f'A idade de {nome} é {idade}')

idades(maria=5, isadora=20, pedro=14)

# Exemplo 2
def jogadas(nome, **kwargs):
    print(kwargs)
    for jogada in kwargs:
        print(kwargs[jogada])
        if kwargs[jogada] == 10:
            return f'{nome} ganhou!'
    return f'{nome} perdeu!'

#print(jogadas('Marcelo', j1=9, j2=8, j3=8, j4=9, j5=6))
print(jogadas('Marcelo', j1=9, j2=8, j3=10, j4=9, j5=6))

# Exemplo de **kwargs com dicionário
def apresentarNotas(**kwargs):
    print(kwargs)
    for aluno in kwargs:
        print(f'{aluno}: {kwargs[aluno]}')

notas = {'joao':7, 'carlos':10, 'jessica':9}
#apresentarNotas(notas) #TypeError
apresentarNotas(**notas)
#apresentarNotas()

# Obs.: Os asteriscos no argumento informam que deve haver um desempacotamento do dicionario,
# antes que o mesmo seja enviado para a função

# Exemplo com dicionário e sem **kwargs
def apresentarNotas(joao, carlos, jessica):
    print(f'Joao: {joao}, Carlos: {carlos}, Jessica: {jessica}')

notas = {'joao': 7, 'carlos': 10, 'jessica': 9}
#notas = {'joao': 7, 'carlos': 10, 'jessic': 9} #TypeError
apresentarNotas(**notas)

# Obs.: Ao passar um dicionario para uma função sem utilizar o **kwargs, os nomes das chaves
# devem ser iguais aos nomes dos parâmetros da função.

# Ordem de utilização de *args e **kwargs

# CORRETA: def função(obrigatórios, *args, default, **kwargs)
# ERRADA: def função(obrigatórios, default, *args, **kwargs)

def certa(nome, *args, cidade='Curitiba', **kwargs):
    print(f'{nome}\n{args}\n{cidade}\n{kwargs}')

def errada(nome, cidade='Curitiba', *args, **kwargs):
    print(f'{nome}\n{args}\n{cidade}\n{kwargs}')

certa('Dudu', 10, 20, 30, estado='Paraná', pais='Brasil')
errada('Dudu', 10, 20, 30, estado='Paraná', pais='Brasil')
