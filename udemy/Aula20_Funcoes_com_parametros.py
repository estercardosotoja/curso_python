"""
Funções com parâmetros:

- Recebem dados e variáveis (argumentos) para utilização em processos internos
- Podem ter inúmeros parâmetros (separados por vírgula)

# Exemplos de funções com parâmetros:
    sun()
    max()
    min()
    index()
    print()
    input()

# Exemplo 1
    def imparPar(numero):
        if numero % 2 == 0:
            print(f'{numero} é par')
            #return f'{numero} é par'
        else:
            print(f'{numero} é impar')
            #return f'{numero} é impar'

    imparPar(10)
    imparPar(27)
    #imparPar() #TypeError

# Exemplo 2
    def soma(num1, num2):
        print(num1 + num2)

    def subtracao(num1, num2):
        print(num1 - num2)

    def divisao(num1, num2):
        print(num1 / num2)

    def multiplicacao(num1, num2):
        print(num1 * num2)

    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))

    soma(n1, n2)
    subtracao(n1, n2)
    divisao(n1, n2)
    multiplicacao(n1, n2)

# Exemplo 3
    def separar(lista):
        for num in lista:
            if num > 10:
                print(num, end=' ')

    listaCriada = [21, 3, 213, 543, 54, 65, 12, 0, 21, 24, 432.121, 532]
    separar(listaCriada)

# Nomear argumentos
    def cidade(parte1, parte2):
        print(parte1 + ' ' + parte2)

    cidade('São', 'Paulo')
    cidade('Paulo', 'São')

    cidade(parte1='São', parte2='Paulo')
    cidade(parte2='Paulo', parte1='São')

# Parâmetro padrão

    #Função que nao exige parâmetros
        print()
        input()

    #Função que exige parâmetros
        def soma(num1, num2):
            print(num1 + num2)

        soma(10, 18)

    #Função com parãmetro padrão (default)
        def medida(numero, referencia=60): #Coloca um valor padrão
            if numero > referencia:
                print(f'{numero} é maior que {referencia}')
            else:
                print(f'{numero} é menor que {referencia}')

        medida(70)
        medida(30)
        medida(40, 30)
        medida(30, 40)
    #Obs.: O parâmetro padrão deve ser sempre o último entre os parâmetros de uma função.

    def medida(numero=75, referencia=60):
        if numero > referencia:
            print(f'{numero} é maior que {referencia}')
        else:
            print(f'{numero} é menor que {referencia}')

    medida()
    medida(40, 30)
    medida(70)

# Variáveis locais e globais para funções
        nome = 'arroz'  # Comando global

        def comida():
            global nome
            nome = nome + ' e miojo'
            print(nome)

        comida()

    #Comando nonlocal (para funções dentro de funções)
        def funFora():
            total = 0
            def funDentro():
                nonlocal total # Conseguimos usar a varivel de função de fora.
                total = total + 1
                print(total)
            return funDentro()

        funFora()
        #funDentro() #NameErrorAula20_Funcoes_com_parametros.py

"""