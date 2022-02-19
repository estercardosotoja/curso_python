"""
Funcoes sem parametros
"""
"""
-O que são funções?
 - São blocos de código que irão executar uma tarefa especifica, podendo ser reutilizavel.
 - Tem por papel organizar,diminuir seu programa e facilitar alterações e gerenciamento.
 - São declaradas após os comentários iniciais e imports(se houver)
 - Já estudamos algumas funções:
     a)print()
     b)input()
     c)type()

como declarar?
    def nome(parametros ou não):
        #Processo

Nessa aula, vamos focar sem parametros:
    def nome():
        #Processo

#Sempre faça o nome da função começar com letras minusculas e se for nome composto, separe po underline(_)
    Ex:
    a)
    def teste_frase(): #Não há parametros de entrada
        print('Estou na funcao')

    teste_frase() #Executar teste_frase,SEMPRE COM PARENTESES

    b)Posso chamar a função onde eu quiser.
    def teste_frase(): #Não há parametros de entrada
        print('Estou na funcao')

for i in range(0,3):
    teste_frase()

Obs: Podemos criar uma variavel do tipo função
Ex:
def teste_frase(): #Não há parametros de entrada
    print('Estou na funcao')

frase = teste_frase #Quando crio variaveis do tipo função, deve ser SEM PARENTESES
print(type(frase))
frase()
#Quando utiliza parenteses, chama a execução da função, sem parenteses apenas chama o objeto função.

Há duas classificações em funções:
1) Função com retorno e sem retorno:
- O retorno é utilizado para justamente retornar alguma operação/variavel de dentro da função
- Para isso utiliza-se a palavra return
- Podemos ter mais de um return na função
Ex:
#Função sem retorno
def operacao():
    contador = 60 #Isso é uma variavel local ou global?? Local
    contador += 2
    print(f'Contador = {contador}')

print(operacao()) #Quando não há return dentro da função retorna None

#Função com retorno
def operacao():
    contador = 60 #Isso é uma variavel local ou global?? Local
    contador += 2
    print(f'Contador = {contador}')
    return contador

print(operacao()) #Agora o valor retornado foi de 62
Obs:Assim que a função reconhece a palavra return, ela finaliza automaticamente
Ex:
def operacao():
    contador = 59
    if contador < 60:
        contador += 2
        return contador
    print(f'Contador = {contador}')
    return contador

print(operacao())

2) Funções recursivas e não recursivas:
O que é recursividade?
 - Aquilo que se repete indefinidamente. Em programação uma função recursiva é aquela que retorna ela mesma.
#Função não recursiva (Não retorna ela mesma, executada apenas 1 vez)
Ex:
def celsius_kelvin():
    celsius = int(input('Digite o valor em Celsius: '))
    kelvin = celsius + 273
    return kelvin

print(celsius_kelvin())

#Função recursiva
def celsius_kelvin():
    celsius = int(input('Digite o valor em Celsius: '))
    kelvin = celsius + 273
    print(f'{kelvin}')
    sair =input('Deseja sair? ')
    if sair == 'sim':
        return 'Acabou'
    else:
        return celsius_kelvin() #Retornando para ela mesma, lembrando de usar os parenteses.

print(celsius_kelvin())

Obs: Lembre-se SEMPRE de uma condição de parada na recursividade. Caso contrário, cairá em um loop infinito.
Vantagem de usar recursão: Torna o código mais limpo e gera sequencia facilmente.
Desvantagens de usar recursão: A lógica pode ser mais complexa e também usar mais memória.
"""
