"""
Generators

- Tuple Comprehension

Gerar um objeto generator a partir do processamento de uma coleção de dados.

Sintaxe: (operação/função for elemento in iterável)

# Exemplos de generators

#Exemplo 1
numeros = list(range(1, 11))
maiores = (numero for numero in numeros if numero > 5)
print(type(maiores))
print(maiores)
for i in maiores:
    print(i, end=' ')

for i in maiores:
    print(i, end=' ')

# Obs.: O objeto generator é perdido após sua iteração

# Exemplo 2
nomes = ('Pedro', 'Tiara', 'Lucas', 'Gustavo', 'Ana')
nome5 = (nome * 2 if len(nome) == 5 else nome for nome in nomes)
print(type(nome5))
print(nome5)
listaNomes5 = list(nome5)
print(listaNomes5)

listaNomes5 = list(nome5)
print(listaNomes5)

# Comparação de ocupação de memória

from sys import getsizeof

#print(getsizeof('Programando Ideias')) #Retorna a memória ocupada em Bytes

#print(getsizeof(10))

# Tamanho de uma List Comprehension
print(getsizeof([num for num in range(1, 1001)]))

# Tamanho de um Generator
print(getsizeof(num for num in range(1, 1001)))

"""