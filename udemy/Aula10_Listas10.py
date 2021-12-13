#Exemplo 1:

lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898') #Torna uma String em uma lista
print(lista6)
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

"""
# Listar a lista 

    lista7 = list(range(1, 11))
    print(lista7)

#Percorrer as listas (interavéis)

#- For
    for elemento in lista2:
        print(elemento, end=' ')    
    total = 0
    
    for elemento in lista2:
        total = total + elemento
    print(f'\nTotal: {total/len(lista2)}')

# - While 
    total = 0
    cont = 0
    while len(lista2) != 0:
        total = total + lista2.pop()
        cont += 1
    print(total/cont)

#Obter indicies da lista 
    jogos = ['Sonic', 'Super Mario', 'GTA', 'GoW', 'PES']
    for indices, jogo in enumerate(jogos):
        print(indices, jogo)
        
#Index
    print(lista2.index(4))
    print(lista2.index(8))
    print(lista2.index(5, 4)) Busca o valor 5 a partir do indice 4 
    print(lista2.index(5, 3, 6)) Busca o valor 5 ENTRE os indice 3 e 6 
    print(lista2.index(80)) #não temos esse valor na lista

#Descompactar Listas
    animal, cor, letra = lista5
    print(animal, cor, letra)

#Funções importantes para trabalhar com listas
    # Apenas para inteiros ou floats  

    print(sum(lista2)) #Soma dos valores das listas
    print(max(lista2)) #Mostra valores maximo das listas
    print(min(lista2)) #Mostra valores minimos das listas

    # Round = Arrendondar os valores da lista
    listaPlana = [2.09304902, 2.98576879843724, 5.39480928409850]
    for elemento in listaPlana:
        print(round(elemento))
        
#Obter o modulo de uma lista
    listanegativa = [-2, -5, -6, 1000]
    for numero in listanegativa:
        print(abs(numero))

 #Copiar uma lista 
    # - Deep Copy = cópias listas e as torna idenpendente entre si, ou seja, qualquer modificação em uma não modifica a outra.
    lista1 = lista2.copy

    # - Shallow Copy      cópias listas e as conecta, ou seja, qualquer modificação em uma modifica a outra.
    print(lista2)
    lista1 = lista2

# Matrizes
    # Sintaxe:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

    # Manipulando por linhas: 
for linha in matriz:
    print(linha)

    # Acessando elementos
print(matriz[0, 1])
print(matriz[2, 1])

    #Acessamentos elementos por repetição
for linha in matriz:
    for numero in linha:
        print(numero)
"""


#Jogo da Velha com Matriz
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print(matriz[0])
print(matriz[1])
print(matriz[2])

linha1 = int(input("Play1 - Digite a linha: "))
coluna1 = int(input("Play1 - Digite a coluna : "))
matriz[linha1][coluna1] = 'X'

print(matriz[0])
print(matriz[1])
print(matriz[2])

linha2 = int(input("Play2 - Digite a linha: "))
coluna2 = int(input("Play2 - Digite a coluna : "))
matriz[linha2][coluna2] = 'O'

print(matriz[0])
print(matriz[1])
print(matriz[2])