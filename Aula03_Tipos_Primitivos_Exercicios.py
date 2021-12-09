"""
1) Relacione as colunas

    1) Inteiros
    2) Float
    3) Complexo
    4) Booleano
    5) String

    ( 5 ) "Casa"
    ( 3 ) 2 + 0j
    ( 4 ) True
    ( 5 ) '123'
    ( 2 ) 1.2345
    ( 4 ) False
    ( 5 ) '''2j'''
    ( 3 ) 10+1j
    ( 1 ) 2
    ( 5 ) 'Programando Ideias'

2) Faça um programa que receba o nome de um aluno e quanto ele tirou na prova de programação, depois imprima em apenas
uma linha o nome no modo title e quanto a pessoa tirou na prova.

"""

nome_Aluno = input('Nome do Aluno: ')
nota_Aluno = input('Nota do Aluno: ')

print(f'{nome_Aluno.title()} tirou {nota_Aluno} ')

