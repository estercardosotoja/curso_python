"""
Loop While

Como declarar?
while condição: #Enquanto essa condição for true faça:
    #Processo ex:

x = True
while x:
    print('Estou rodando')
    x = False

    ex 2:
pedido = ''

while pedido != 'quero sair':
    pedido = input('voce não vai sair: ')

 O loop While, diferente do loop for, precisa de uma condição de uma parada definida pelo programador.
A palavra break executa a finalização do loop while.

contador = 0

while contador < 9:
    print(contador,end = ' ')
    contador = contador + 1
    if contador == 5:
        break

Dicas de Ouro:
    1) Podemos escrever um loop while em uma linha caso a codificação seja simples:
        Para isso, separe, prints, operações matemáticas com pornto e virgula.

        contador = 0
        while contador < 9: print(contador, end = ' '); contador = contador + 1;

    2) Palavra continue (Proseguir)
    Caso você tenha uma condição que precise apenas de mandar o loop se repetir escreva continue.
    Ex:
        contador = 0

        while contador < 9:
            print (contador, end = ' ')
            contador += 1
            if contador == 5:
                continue


for                                                    x                            While
Numero de interações depende da sua sequencia               Numero de interações ilimitado
Utiliza um contador que automaticamente se incrementa       Pode utilizar o contator , sendo necessário ser declarado por fora e incremente dentro da condiçõa

                            Os dois são permutaveis , pode ser usado nas mesmas situações.

"""


