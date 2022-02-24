"""
Dicionario
"""
"""
Quando usar dicionario?
    - Dicionarios são interessantes quando voce possui um conjunto de informações de um mesmo objeto ou pessoa.
    Ex:
Funcionarios:
    Paula,27 anos, Programadora
    Gabriel,30 anos, Engenheiro

    #Listas
        funcionarios = []
        list1 = ['Paula',27,'Programadora']
        list2 = ['Gabriel',30,'Engenheiro']
        funcionarios.append(list1)
        funcionarios.append(list2)
        print(funcionarios)
        print(funcionarios[0][1])
    
    #Tuplas
        tuple1 = ('Paula',27,'Programadora')
        tuple2 = ('Gabriel',30,'Engenheiro')
        funcionario = (tuple1,tuple2)
        print(funcionario)
        print(funcionario[1][1])
    
    #Dicionario
        funcionario = {}
        dict1 = {'nome':'Paula','idade':27,'funcao':'Programadora'}
        dict2 = {'nome':'Gabriel','idade':30,'funcao':'Engenheiro'}
        funcionario['Paula'] = dict1
        funcionario['Gabriel'] = dict2
        print(funcionario)
        print(funcionario['Paula']['idade'])
        #Dessa forma sabemos o jeito mais eficaz de encontrar informações

    #Limpar dicionarios com o método clear():
        Ex:
        dicionario = {'Programando':'Ideias'}
        dicionario.clear() #Apenas limpa, não apaga o dicionario completamente
        print(dicionario)
        dicionario['Programando'] = 'Ideias'
        print(dicionario)

    #Shallow Copy x Deep Copy
        a)Deep Copy(Cópia profunda): Copy()
        Ex: #Cada dicionario trabalha separadamente
        dicionario = {'Programando':'Ideias'}
        novo = dicionario.copy()
        novo['Melhor'] = 'do Mundo'
        print(novo)
        print(dicionario)
    
    b)Shallow Copy(Cópia superficial):
        Ex: #Não separa cada dicionario ao ser manipulado
        dicionario = {'Programando':'Ideias'}
        novo = dicionario
        novo['Melhor'] = 'do Mundo'
        print(novo)
        print(dicionario)

    #É possível iterar dicionarios:
        Ex:
        personagem = {'Nome':'Rick','Funcao':'Cientista','Neto':'Morty'}
        for item in personagem:
            print(item) #Retorna as chaves
        for item in personagem:
            print(personagem[item]) #Retorna os dados em cada chave
        
    #Método keys():
        personagem = {'Nome':'Rick','Funcao':'Cientista','Neto':'Morty'}
        print(personagem.keys()) #Retorna uma lista com as chaves
        
    #Método values():
        personagem = {'Nome':'Rick','Funcao':'Cientista','Neto':'Morty'}
        print(personagem.values()) #Retorna uma lista com os elementos do dicionario
        
    #Método items():
        personagem = {'Nome':'Rick','Funcao':'Cientista','Neto':'Morty'}
        print(personagem.items()) #Retorna uma lista onde cada indice é uma tupla de chave e dado
        for chave,dado in personagem.items():
            print(chave)
            print(dado)
        
    #Método len():
        personagem = {'Nome':'Rick','Funcao':'Cientista','Neto':'Morty'}
        print(len(personagem))
        
    # Max,Min,Sum: Máximo,Minimo e Somatório
    #Apenas aceitam dados numericos. Caso utilize string fará uma comparação do tamanho da palavra e o peso de cada letra.
        Ex: #Lembre-se de usar o método values() ou keys() caso queira os elementos nas chaves ou dados.
        dict = {'a':1,'b':2,'c':3}
        print(max(dict.values()))
        print(min(dict.values()))
        print(sum(dict.values()))
"""
