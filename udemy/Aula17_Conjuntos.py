"""
Sets(Conjuntos)
"""
"""
Caracteristicas de conjuntos:
    1)Não são ordenados.
    2)Não aceitam elementos repetidos.
    3)São representados por chaves {}, porém não possuem a relação chave->dado.

Qual a vantagem de utilizar conjuntos?
    - Conjuntos apresentam formas otimizadas de realizar funções especificas que só ele possui.
    - Como inersecção, junção e outros...

Quando utilizar?
     - São utilizados quando você não precisa se preocupar com:
     - ordenação e  repetição de elementos.

Como declarar?
    # Forma 1: (Mais usada):
        nome = {dado1,dado2,dado3,...}
        Ex:
        conjunto = {1,2,3,4,5,6,6,6,6} #Aceitará apenas um numero 6.
        print(conjunto)
        print(type(conjunto))

    # Forma 2: Função set()
        nome = set(iteravel)
        Ex:
        list = [1,2,3,4]
        conjunto = set(list)
        print(conjunto)
        print(type(conjunto))
        OBS1: Não é ordenado e se colocar string fica desordenado.
        OBS2: Sempre colocar uma valor interável, se colocar por exemplo {1} apresentará erro.

#Exemplos:
    - Conjuntos são iteráveis, logo podemos aplicá-los no for:
        pares = {2,4,6,8,10,12,14}
        for num in pares:
            print(num)
    
    - Método in(dentro):
        nome = {'Ana','Bruno','Flavio'}
        print('Ana' in nome) #Retorna True se a Ana está no conjunto
    
    - Adicionar elementos dentro do conjunto:
        esportes = {'Fut','Vol','Nat'}
        esportes.add('Futsal') #Para usar: variavel.add(elemento a ser adicionado)
        print(esportes)

- Remover elementos do conjunto:
    #Forma 1: Remove()
        conjunto = {1,3,5,7,9,11}
        retorno = conjunto.remove(7) #variavel.remove(elemento a ser removido), NÃO O INDICE POIS SETS SAO DESORDENADOS
        print(conjunto)
        print(retorno) #Retorna None, não retorna o elemento deletado
    
    #Forma 2: Discard()
        conjunto = {1,3,5,7,9,11}
        retorno = conjunto.discard(5) #variavel.discard(elemento a ser removido), NÃO O INDICE POIS SETS SAO DESORDENADOS
        print(conjunto)
        print(retorno) #Retorna None, não retorna o elemento deletado
    
    #Forma 3: Pop()
        conjunto = set('Homem de aco')
        retorno = conjunto.pop() #Método pop() não necessita de mandar elementos, assim ele irá remover um valor arbitrário
        print(conjunto)
        print(retorno) #Retorna o dado que foi reomovido
    
    #Forma 4: Clear()
        conjunto = {1,3,5,7,9,11}
        conjunto.clear() #Limpa o conjunto, mas não o apaga
        print(conjunto)
        conjunto.add(1)
        print(conjunto)

    #Função len(): #Retorna o comprimento(numero de elementos) do conjunto
        conjunto = {1,3,5,7,9,11}
        print(len(conjunto))

    # Intersecção de conjuntos (Valores que popssuem em ambos): Intersection()
        # Ex: Mais formal
        notaFabio = {5,6,7}
        notaClara = {6,7,8}
        print(notaClara.intersection(notaFabio)) #Retorna um conjunto com os valores em comum dos dois
        # Curiosidade: Informal
        notaFabio = {5,6,7}
        notaClara = {6,7,8}
        print(notaClara & notaFabio) #Retorna um conjunto com os valores em comum dos dois

    - Uniao de conjuntos (Junta todos os valores de um e outro): union()
        # Ex: Mais formal
        notaFabio = {5,6,7}
        notaClara = {6,7,8}
        print(notaClara.union(notaFabio)) #Retorna um conjunto com todos os valores contidos nos dois
        Curiosidade: Informal
        notaFabio = {5,6,7}
        notaClara = {6,7,8}
        print(notaClara | notaFabio) #Retorna um conjunto com todos os valores contidos nos dois

    - Diferença entre dois conjuntos (Elementos que possuem em apenas um deles): Difference()
        notaFabio = {5,6,7}
        notaClara = {6,7,8}
        print(notaClara.difference(notaFabio)) #difference retorna um conjunto da diferença entre dois conjuntos
        #Pega todos os elementos que estão em notaClara e não estão em notaFabio.

    - Shallow Copy x Deep Copy:
        a)Deep Copy: copy()
        #Cada conjunto vai trabalhar separadamente
            Ex:
            conjunto = {'vish','deu ruim','deep copy'}
            conjunto_novo = conjunto.copy()
            conjunto_novo.add('entendi')
            print(conjunto)
            print(conjunto_novo)
    
        b)Shallow Copy:
        #Altera um conjunto também altera o outro
            Ex:
            conjunto = {'vish','deu ruim','deep copy'}
            conjunto_novo = conjunto
            conjunto_novo.add('entendi')
            print(conjunto)
            print(conjunto_novo)

    - # Max,Min,Sum:
        Ex:
        valores ={1,6,2,8,3,7,11,25,88}
        print(max(valores))
        print(min(valores))
        print(sum(valores))
"""
