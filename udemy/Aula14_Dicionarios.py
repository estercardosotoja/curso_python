"""
Dicionario

    - São apresentados por {}
    - Possuem uma relação chave->elemento.
    - Dicionarios permitem qualquer tipo de dado (int,float,string,...)
    - Não são ordenados pelas chaves.
    - São utilizados para otimizar a busca de dados, pois basta você saber a chave que irá acessar o elemento.

    Sintaxa: { 'Chave1': 'Valor1', 'ChaveN': 'ValorN'}
    
Como declarar?

    # Forma 1(Mais usada):
        Ex: times_futebol = {'RJ':'Flamengo','SP':'Corinthians'}
        
    #Poderia também:
        Ex: times_futebol = {
            'Rj':'Flamengo',
            'SP':'Corinthians'
        }
        print(times_futebol)
        print(type(times_futebol))

    #Forma 2(Utilizando o comando dict()):
        Ex: times_futebol = dict(RJ='Flamengo',SP='Corinthians')
        print(times_futebol)
        print(type(times_futebol))
        
    #Forma 3(Menos utilizada): #fromkeys()
    Cria um dicionario com cada item dentro do iterável com o mesmo elemento.
        nome = {}.fromkeys(iterável,elemento)
        Ex:
        times_futebol = {}.fromkeys([0,1,2,3],'dado') // retorna: {'0':'dado', '1':'dado', '2':dado, '3':'dado'}
        print(times_futebol)

    -> Sobre as chaves:
        - Devem ser únicas.
        - Podem ser de qualquer tipo. (string, int, float, array, etc..)

    -> Sobre os dados:
        - Podem ser duplicados.
        - Podem ser de qualquer tipo.
        Ex:
        times_futebol = {'RJ':'Flamengo','SP':'Flamengo'} #Imprime ambos
        print(times_futebol)
        times_futebol = {'RJ':'Flamengo','RJ':'Corinthians'} #Imprime apenas um dos elementos
        print(times_futebol)

# Formas de acessar elementos:

    # Forma 1:
        Ex:
        times_futebol = {'RJ':'Flamengo','SP':'Corinthians'}
        print(times_futebol['SP']) 
        #Nesse método caso a chave não exista resultará em KeyError.

    # Forma 2:
        Ex:
        times_futebol = {'RJ':'Flamengo','SP':'Corinthians'}
        print(times_futebol.get('RJ')) #Pegue dentro de times_futebol o elemento dentro da chave 'RJ'
        #Caso a chave não exista retorna tipo None

        times_futebol = {'RJ':'Flamengo','SP':'Corinthians'} #Mais usada
        print(times_futebol.get('BH','outra chave')) #Retorna 'outra chave' caso a chave que voce pesquise não exista

        times_futebol = {'RJ':'Flamengo','SP':'Corinthians'}
        print('BH' in times_futebol) #Retorna True se a chave existir e False se não existir

O que é None?
     - É um tipo de dado sem tipo.
     - Usado para declarar variáveis que vocÊ ainda não sabe o tipo que irá utilizar.
        Ex:
        dado = None
        print(type(dado))
        dado = 's'
        print(type(dado))

#Adicionar/alterar elementos dentro do dicionário
    Ex:
        # Forma 1(Mais otimizada):
            sagas = {
                (1,2):'HP',
                (3,4):'PJ',
                (5,6):'JV'
            }
            sagas[(7,8)] = 'MR'
            sagas[(1,2)] = 'Digimon'
            print(sagas)

        # Forma 2 (Função update()):
        sagas = {
            (1,2):'HP',
            (3,4):'PJ',
            (5,6):'JV'
        }
        dado_novo = {(7,8):'MR'}
        sagas.update(dado_novo)
        sagas.update({(1,2):'Digimon'})
        print(sagas)

#Removendo valores do dicionario:
    pokemon = {
        'Agua':'Squirtle',
        'Fogo':'Chamander',
        'Grama':'Bulbassauro'
    }

    # Forma 1: Função pop()
    dado = pokemon.pop('Agua')
    print(dado)
    print(pokemon)
    #O método pop() permite retornar o dado dentro da chave podendo utilizar o elemento posteriormente.

    # Forma 2: Palavra del
    dado = del pokemon['Agua'] #Dará erro pois o correto é utilizar del pokemon['Agua']
    print(dado)
    print(pokemon)
    #Não é possível retornar o dado dentro da chave por esse método
    """
