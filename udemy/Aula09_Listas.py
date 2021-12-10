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
    