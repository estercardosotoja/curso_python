"""
Modos de abertura de arquivo

Existem outros métodos para abertura de arquivos além do read e write, eles podem ser consultados em:
https://docs.python.org/3/library/functions.html#open
a) x-> Abre para escrita apenas se o arquivo não existir. Se já existir gera um erro do tipo FileExistsError(Arquivo já existe)
Ex:
"""

try:
    with open('frutas.txt','x') as arq:
        arq.write('Banana\n')
        arq.write('Uva\n')
except FileExistsError:
    print('O arquivo ja existe')

"""
b) a -> Abre para escrita acrescentando SEMPRE ao final do arquivo se ele existir, caso não exista ele cria um novo e adiciona
        normalmente.
- Nós não temos controle do cursor
Ex:
"""

with open('herois.txt','a') as arq:
    arq.write('Superman\n')
    arq.write('Batman\n')
    arq.seek(0) #Não adianta controlar o cursor porque sempre imprime no final
    arq.write('Homem de Ferro\n')

"""
c)'+' -> Abrir para atualização de leitura ou escrita.
- r+:Arquivo já deve existir. Temos o controle do cursor e podemos escrever além de ler o arquivo.
- w+:Cria um novo arquivo caso não exista e sobrescreve o texto caso já exista. Tambem realiza leitura alem da escrita de
      arquivos. Temos o controle do cursor.
- a+:Cria um novo arquivo caso não exista e adiciona o texto no final caso já exista. Realiza leitura e escrita.
     Temos o controle do cursor apenas para realizar a leitura, mas não conseguimos escrever no inicio do arquivo
    mesmo utilizando-o.
- x+: Cria um novo arquivo caso ele não exista. Caso o arquivo já existir gera FileExistsError. Podemos realizar leitura
      e escrita. Temos controle do cursor para realizar escrita e leitura.
Ex:
"""

with open('herois.txt', 'x+') as arq:
    arq.write('Superman\n')
    arq.write('Batman\n')
    arq.seek(0)
    arq.write('Capitao America\n')

