""""""
"""
Escrita em Arquivos

#Obs.: Ao abrir um arquivo pelo modo padrão, é possível apenas realizar a leitura.
# arquivo = open('Lucros.txt')

- Para escrita, é necessário alterar o modo de abertura de 'r' para 'w' - write

#Obs.: Sempre que houver escrita em um arquivo pelo modo 'w', ele será criado caso não exitir. 
Caso já exista, seu conteúdo será substituído completamente.
"""

# Escrever em arquivos
arquivo = open('Aula86_EscreverEmArquivosExemploAula.txt', 'w')

arquivo.write('Café: R$ 15.800,00')
arquivo.write('\nBiscoitos: R$ 24.350,00')

arquivo.close()

arquivo = open('Despesas.txt', 'w')
arquivo.write('\nBolachas: R$ 12.000,00')
arquivo.close()

# Modo pythônico de trabalhar com arquivos
with open('Aula86_EscreverEmArquivosExemploAula.txt', 'w') as desp:
    desp.write('Café: R$ 15.800,00')
    desp.write('\nE banana tbm')

# Escrever em arquivos com entrada de dados
with open('Aula86_EscreverEmArquivosExemploAula.txt', 'w') as desp:
    while True:
        palavra = input("Digite uma palavra ou 'sair': ")
        if palavra == 'sair':
            break
        else:
            desp.write(palavra + '\n')


