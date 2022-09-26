""""""
"""
Lambdas

- São como funções sem nome que funcionam como uma função qualquer.

Sintaxe: lambda parâmetro(s): retorno

# Exemplo de uma função normal
    def pot(x, y):
        return x ** y
    
    print(pot(3, 2))

# Exemplo 1 de expressão lambda
    pot = lambda x, y: print(x ** y)
    pot(3, 2)

# Obs.: Expressões lambdas aceitam qualquer quantiade de parâmetros de entrada.

# Exemplo 2 de expressão lambda

    cadastro = lambda nome, idade: f'Nome: {nome.title()}\nIdade: {idade}'
    print(cadastro('Pedro', 24))
    
    #print(cadastro('Pedro', 24, 32)) #TypeError

# Exemplo 3 de expressão lambda
    segGrau = lambda a, b, c, x: a * x ** 2 + b * x + c
    print(segGrau(1, 5, 8, 3))

# Outro modo de fazer o Exemplo 3
    def quadratica(a, b, c):
        return lambda x: a * x ** 2 + b * x + c

    segGrau = quadratica(1, 5, 8)
    print(segGrau(3))
"""