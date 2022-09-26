""""""
"""
Seek e ReadLine

- Seek: Movimenta o cursor pelo arquivo
"""

arquivo = open('Lucros.txt')
print(arquivo.read())

print(arquivo.read())

arquivo.seek(0) #Move o cursor para o início do arquivo
print(arquivo.read())

arquivo = open('Lucros.txt')

arquivo.seek(5)
print(arquivo.read())

# readline: Lê o arquivo por linhas

arquivo = open('Lucros.txt')
linha = arquivo.readline()
print(linha)
linha = arquivo.readline()
print(linha)

# readlineS: Retorna uma lista em que cada elemento é uma linha do arquivo

arquivo = open('Lucros.txt')
listaLinhas = arquivo.readlines()
print(listaLinhas)

