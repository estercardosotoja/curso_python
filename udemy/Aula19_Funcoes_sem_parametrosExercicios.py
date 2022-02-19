"""
1) Foi realizada uma pesquisa de algumas características e gostos de quatro
habitantes incluindo: nome, sexo, esporte favorito (Natação, Futebol, Volêi,
Tênis) e idade. Com esses dados faça:
- Função que armazene os dados em uma lista. Dica: Use dicionários dentro da
lista.
- Calcule a idade média de homens que gostam de natação. Caso não haja
homens que gostam de natação chame uma função e imprima um aviso de que
não há homens que gostam de natação0
"""

def questionario():
    nome = ''
    dados = dict(nome=input("Nome do habitante:"),
                 sexo=str(input("Nome do sexo:")),
                 esporte=escolha_esporte(),
                 idade=int(input("Idade:")))
    return dados

def escolha_esporte():
    opcao = input("Digite o codigo refente ao esporte \n 1 - Natação, \n 2 - Futebol, \n 3 - Volêi, \n 4 - Tênis ")
    if opcao == "1":
        return "Natação"
    elif opcao == "2":
        return  "Futebol"
    elif opcao == "3":
        return "Volei"
    elif opcao == "4":
        return "Tenis"
    else:
        print('OPCAO INVALIDA')
        return

def inicio():
    sair = ('')
    habitantes.append(questionario())
    sair = input(" Adicionar mais alguém? s/n")
    if sair != "n":
        inicio()
    else:
        print(f"Fim \n Habitantes {habitantes}")

def aviso():
    print("Não há homens que gostam de natação")

habitantes = []
soma = 0
inicio()
cont = 0
print(habitantes.get('sexo'))
for habitante in habitantes:
    if habitante.get('sexo') in habitante:
        if habitante.get('natacao') in habitante:
           soma =+ habitante.get("idade")
           cont = cont + cont;
    else:
        aviso()

print("Fim")



