"""
List Comprehensions
Gerar uma lista a partir do processamento de uma coleção de dados.
Sintaxe: [operação/função for elemento in interável]

#Exemplo de List Comprehensions

    #Sem List  Comprehensions
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pares = []
#Loop for

for num in impares:
    pares.append(num*2)
print(pares)

 # Com List  Comprehensions
pares = [num * 2 for num in impares]
print(pares)

    # Resumindo mais ainda: print(num * 2 for num in impares)

# List Comprehensions em Estruturas Condicionais

#   IF
numeros = list(range(1, 11))
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print(f' Pares: {pares} \n Impares: {impares}')

#   Else
numeros = list(range(1, 11))
nova = [num if num <= 5 else num * 10 for num in numeros]
print(nova)

# Comprehensions Matrizes
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(f'{num}', end=' ') for num in linha] for linha in matriz]

matriz3 = [[num * 3 for num in linha] for linha in matriz]
print(f'\n Matriz multiplicada por 3 * \n {matriz3}')

"""
