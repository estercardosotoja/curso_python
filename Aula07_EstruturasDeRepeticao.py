"""
Loop for
O for (para) é uma das ferramentas que realizam loop (várias vezes a mesma tarefa).

Como declarar em Python ?

    for item in sequencia:
        #Processo

Para cada item dentro de uma sequencia faça:
    #Processo

A sequencia deve ser iterável, mas o que é isso?
 - são um conjunto de dados que podem ser desmembrados.

 Exemplos de dados iteráveis:
 a)  Strins (Podem ser desmembradas por cada caracter)
        "Filmes" -> 'F','i','l',....
     Relembrando: Podemos pegar caracterespelo inidices da String
     Ex:.
     nome = 'Samatha'
     print(nome[6]) # Irá imprimir o h

    Curiosidade:
    S a m a n t h a
    0 1 2 3 4 5 6 7
   -8-7-6-5-4-3-2-1

     nome = 'Samatha'
     print(nome[2:-2]) # Não irá imprimir
    Obs: Não é possivel imprimir nome [-2:1], o python não fará a leitura quando o primeiro valor estiver casas a frente do mesmo valor

b) Listas , tuplas, dicionários e sets(conjuntos):
    Ex:
    nome = [1,2.0,5,True,'sim']
    nome-> '1','2.0', '5', 'True', 'sim'

c) Função Range();
O que ela faz?
    - Função que cria um intervalo de números escolhido pelo usuário.
    Ex:
    range(numero que deseja o inicio, numero final+1)
    numero = range(2,10)
    print(numero)

#Complemento
    O range() pode ser utilizado por diveras formas:
        a) range(2,10) #Cria uma sequencia de 2 a 9
        b) range(10) #Cria uma sequencia de 0 a 9
        c) range(-4,5) #Cria uma sequencia de -4 a 4
        d) range(3,19,3) #Cria uma sequencia de 3 a 18 ao passo 3
        e) range(18,4,-3) #Cria uma sequencia de 18 a 3 ao passo 3 negativo

# É possível utilizar condicionais dentro do loop:
#Achando numeros pares dentro de uma sequencia
for numero in range(2,20):
    if numero % 2 == 0: # Se o resto da divisão de numero por 2 for zero faça:
        print(f'Achei um numero par, numero:{numero}')
#Exemplo mais complexo, é possível ter for's consecutivos:
fruta ="abacate"
valor = range(1,4)
for letra in fruta:
    if letra == 'a':
        for num in valor:
            print('Achei a letra a')
Para sair antes que todo o loop seja executado, podemos utilizar a palavra break(Pausa).
Ex:
string = 'abcdefghijkl'

for letra in string:
    print(letra,end='/')
    if letra == 'g':
        break
Para prosseguir o loop utilizamos a palavra continue(prosseguir).
Ex:
string = 'abcdefghijkl'

for letra in string:
    if letra == 'g':
        continue
    print(letra,end='/')

Por fim, método enumerate():
O que faz?
- Basicamente adiciona um contador para cada elemento que foi desmembrado na sequencia.
Para declarar faça:
enumerate(variável)
# Ex:
heroi = 'Batman'
#Ao usar o enumerate
(0,'B'),(1,'a'),(2,'t'),...
for valor in enumerate(heroi):
    print(valor)
for contador,letra in enumerate(heroi):
    print(f'A {contador+1} letra e:{letra}')
for valor in enumerate(range(3,7)):
    print(valor)
for contador,letra in enumerate(range(3,7)):
    print(f'O {contador+1} numero e:{letra}')
"""

#Aplicação com String
seriado = 'Todo mundo odeia o Cris'
for letra in seriado:
    print(letra, end='\t ')
print('\n')

#Aplicação com Listas
num = [1, 2, 'oi', 'True']
for elemento in num:
    print(elemento)
print('\n')

#Aplicação range()
intervalo_num = range(3,11)
for numero in intervalo_num:
    print(numero)

