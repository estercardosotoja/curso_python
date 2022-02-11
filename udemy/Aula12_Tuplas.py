"""
Tuplas

As tuplas são muito parecidas com listas, há duas diferenças:
    1 - Não pode remover ou adicionar dados, apenas sobreescrever;
    2 - Enquanto as listas são com [] 'colchetes' as tuplas são com () 'parenteses'
    Sintaxe: (elemento, elemento1, elemento2,...,elementoN) ou elemento, elemento1, elemento2,...,elementoN
    obs: o que determina uma tupla são as virgulas

    Vantagens das Tuplas
     - São mais seguras para os dados;
     - São mais rápidas para serem processadas;
     - Em duplas não há Shallow Copy = Cópias listas e as conecta, ou seja, qualquer modificação em uma modifica a outra.
     Então sempre serão idependentes entre si.

    ex:  #TEM QUE TER A VITGULAAAHHH
    tuplas1 = (1, 2, 3, 4, 5)
    tuplas2 = (1,)
    tuplas3 = 1, 2, 3, 4, 5
    tuplas4 = 1,
    tuplas5 = ('futebol', 'moto', 'França')
    tuplas6 = ('pizza', True , 18, 5j, 0.43, 'x', True)
    tupla7 = tuple(range(11))
    tupla8 = tuple(['azul', True, 'z', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])
    print(tupla8)

    print(type(tuplas1), type(tuplas2), type(tuplas3), type(tuplas4))

    Quando usar?
    - Quando não for necessário realizar modificações nos dados
    Exemplo: Calendário = meses, dias do ano.

    # FUNÇÕES
    ** As funções são muito parecidas que as usadas em listas, porém como não há adição ou exclução de dados, nem todas as funções usadas em Lista são usadas em Tuplas.

    # Concatenação duas ou mais tuplas:
        ex.: tuplanova = tuplas1 + tuplas5
             print(tuplanova)
,
        ex:. tuplas1 = tuplas1 + tuplas5
        print(tuplas1)

        OBS: A primeira tuplas1 foi apagada, e assim foi criada uma nova no momento da concatenação.

    # Verificar valor está na tupla
        ex:. print(10 in tuplas8)
             print(False in tuplas8)

    #Obter a quantidade que um valor se repete em tupla
    ex.: cores = ('branco', 'azul', 'preto', 'verde', 'amarelo', 'verde')
         print(cores.count('verde'))

    #Acessar elementos de uma tupla
    ex.: print(tuplas8[2]);
         print(tuplas8[4]);
         print(tuplas8[-2]);
         print(tuplas8[-4]);

    #Percorrer Tuplas (Iterar):

        #FOR
        for elemento in tupla1:
            print(elemento, end=' ')
        total = 0
        for elemento in tuplas1:
            total = total + elemento
        print(f'\n{total/len(tuplas1)}')

        #WHILE
        total = 0
        cont = 0
        while cont < len(tuplas1):
            total =+ tuplas1[cont]
            cont =+ 1
        print(total/cont);

    #Obter indice da tupla:
        for indice, cor in enumerate(cores)
            print('f{indice}:{cor}')

    #FUNÇÕES ÚTEIS PARA SE TRABALHAR COM TUPLAS
    **OBS: apenas para inteiros e floats
       print(sum(tuplas1)) #Retorna a soma dos elementos
       print(max(tuplas1)) #Retorna o maior valor dos elementos
       print(min(tuplas1)) #Retorna o menor dos elementos

    ** OBS: para qualquer tipo de dado:
       print(len(tuplas1)) #Tamanho da tupla

    #Copiar uma tupla:
        tuplaNova = tuplas1
        print(tuplaNova)


"""

tuplas1 = (1, 2, 3, 4, 5)
tuplas2 = (1,)
tuplas3 = 1, 2, 3, 4, 5
tuplas4 = 1,
tuplas5 = ('futebol', 'moto', 'França')
tuplas6 = ('pizza', True, 18, 5j, 0.43, 'x', True)
tuplas7 = tuple(range(11))
tuplas8 = tuple(['azul', True, 'z', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])
print(tuplas8)

