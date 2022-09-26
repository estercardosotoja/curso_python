""""""
"""
Leitura de Arquivos

#Abrir um arquivo

#Função Open: Recebe como parâmetro obrigatório o endereço em que se encontra o arquivo.

#Obs.: A abertura padrão é do modo leitura (mode 'r' - read)

"""

arquivo = open('Lucros.txt')

#print(arquivo)

#<_io.TextIOWrapper name='Lucros.txt' mode='r' encoding='cp1252'>

#Ler um arquivo
print(arquivo.read()) # Função Read realiza a leitura do arquivo
print('_________________________________________________')
print(arquivo.read())

arq = arquivo.read()
print(type(arq)) #String

#Delimitando a quantidade de caracteres (avanços do cursor)
arquivo = open('Lucros.txt')
print(arquivo.read(5))

#Fechar um arquivo

arquivo = open('Lucros.txt')

print(arquivo.closed)
arquivo.close() #Finaliza a conexão entre o arquivo aberto e o PyCharm (streaming)
print(arquivo.closed)

print(arquivo.read()) #ValueError

#Modo pythônico de trabalhar com arquivos
with open('Lucros.txt') as luc:
    print(luc.closed)
    print(luc.read())

print(luc.closed)
#print(luc.read())#ValueError
