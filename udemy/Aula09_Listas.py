"""
Listas
Uma coleção de dados muiito poderosa e importante.
Em C - Vetores e Matrizes : Apenas m tipo de dados e tamnho unico.
Em Python as Listas
    - São dinamicas e podem receber qualquer tipo de dados
    - Tamanho limitado á memória disponivel do seu PC.
Sintaxe: [elemento1, elemento2 , ...., elementoN]
"""
#Exemplo 1:

lista1 = []
lista2 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista3 = [3.4, 23.42, 532.12]
lista4 = [True, False, True, True]
lista5 = ['tatu', 'roxo', 'a']
lista6 = list('Silvio Santos 1898') #Torna uma String em uma lista
print(lista6)
lista7 = [43, True, 23.1, 'abacate', 'Russia', 12, 'x', False, [1, 3, 5, 7]]

cor = 'azul'
animal = 'palvão'
numero = 42
lista8 = [cor, animal, numero]


        #Adicionando valores em uma lista
    # -- Append: Adiciona apenas 1 elemento por vez, no final da lista ... OBS: Sempre adiciona o objeto.

print(lista2)
lista2.append(6)
print(lista2)

    # -- Extend: Adiciona multiplos valores por vez.
    # OBS:  Recebe apenas iteráveis e adiciona elementos do mesmo.
    # OBS:  Recebe apenas um iteravel por vez

print(lista5)
lista5.extend(['abacaxi', 1.98, 'Kg'])
print(lista5)

    # -- Insert: Adiciona um valor em um determinado indice de uma lista
    #OBS.: Este comando não substitui o valor original, apenas desloca-o para a direita

lista4.insert(1, 'Aqui')
print(lista4)

    #-- Concatenar duas (ou mais) listas

listasSomadas = lista2 + lista4
print(listasSomadas)

        # Converter Strings em listas

    # Split --  Cria uma lista separando uma String por seus espaços (' ') (padrão)

frase = ('Hoje é umn novo dia, de um novo tempo que começou')
lista9 = frase.split()
print(lista9)

#OBS: É possivel indicar o parametro de separação
lista9 = frase.split(',') #No caso irá separa onde temos a virgula
print(lista9)

lista9 = frase.split('novo') #No caso irá separa onde temos a palavra novo
print(lista9)

    #Join -- Cria uma string juntando os elementos de uma lista
lista10 = ['Silvo', 'Santos', 'vem', 'ai']
frase = ' '.join(lista10)
print(frase)

lista10 = ['Silvo', 'Santos', 'vem', 'ai']
frase = '@'.join(lista10)
print(frase)

    #Contar a quantidade de elementos de uma lista
print('A quantidade de elementos na lista7 é : ', len(lista7))

    #Verificar se determinado valor está na lista

if 'x' in lista7:
    print('x na lista7')
else:
    print('x não está na lista')

print('x' in lista7) #Retorna true or false

    #Count - Verificar a quantidade de vez que um item se repete em uma lista

print(lista6)
quantidade = lista6.count('8')
print(f'Eu encontrei {quantidade} vez/vezes')

    #Sort - Ordenar uma lista
# OBS: NÃO ORDENA INTEIROS COM STRING JUNTO
# OBS: Considera o tamanho da String
lista11 = [12, 43, 453, 345, 3, 45, 3, 534, 53, 6, 5, 56, 7, 8, 8, 5, 43, 5, 23, 4, 2]
print(lista11)

lista11.sort()
print(lista11)

lista12 = ['vc', 'a', 'avian']
lista12.sort()
print(lista12)

    #Reverse - Inverte a ordem de uma lista
print(lista7)
lista7.reverse()
print(lista7)

    #Slicing - Outra maneira de inverter a ordem
print(lista6)
print(lista6[::-1])

        #lista[inicio:fim:passo]
print(lista7)
print(lista7[2:])
print(lista7[2:5:2])

        #acessar elementos da lista
print(lista7[2])
print(lista7[-2]) #É como se a lista fosse um circulo, então a posição negativa seria o fim o array para inicio.

#print(lista7[15]) #Não tem este index na lista então apresenta erro
#print(lista7[-15])

for ind in range(0, 3):
    print(lista7[ind])

    #Substituir elemento de uma lista
print(lista7)
lista7[1] = False
lista7[4] = 'Vodka'
print(lista7)

# Remover elementos de uma lista

    #POP = Remove o último elemento de uma lista
    #obs: retorna o elemento removido

print(lista2)
print(lista2.pop())
print(lista2)

    #obs: é possivel determinal qual elemento querems excluir da lista

print(lista2)
print(lista2.pop(5))
print(lista2)


#Repetir elementos de uma lista
print(lista4)
lista4 = lista4 * 4
print(lista4)

#Limpar uma lista
print(lista3)
lista3.clear()
print(lista3)
