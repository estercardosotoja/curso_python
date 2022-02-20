"""

    1) Foi realizada uma pesquisa de algumas características e gostos de quatro habitantes incluindo:
    nome, sexo, esporte favorito (Natação, Futebol, Volêi, Tênis) e idade. Com esses dados faça:
    - Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
    - Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam
    de natação chame uma função e imprima um aviso de que não há homens que gostam de natação

"""

def questionario():
    nome = ''
    dados = dict(nome=input("Nome do habitante:"),
                 sexo=str(input("Nome do sexo:")),
                 esporte=escolha_esporte(),
                 idade=int(input("Idade:")))
    return dados

def escolha_esporte():
    opcao = (input("Digite o codigo refente ao esporte \n 1 - Natação, \n 2 - Futebol, \n 3 - Volêi, \n 4 - Tênis \n Opção: "))
    if opcao == "1":
        return "natacao"
    elif opcao == "2":
        return  "futebol"
    elif opcao == "3":
        return "volei"
    elif opcao == "4":
        return "tenis"
    else:
        print('OPCAO INVALIDA')
        return

def inicio():
    sair = ('')
    habitantes.append(questionario())
    sair = input("Adicionar mais alguém? s/n")
    if sair != "n":
        inicio()
    else:
        print(f"Fim \n Habitantes {habitantes}")

def aviso():

    return "Não há homens que gostam de natação"

def respostas():
    total = len(habitantes)
    print(total)
    i = 0
    soma = 0
    homens_natacao = 0
    for i in range(total):
        if habitantes[i]['sexo'] == 'm' and habitantes[i]['esporte'] == 'natacao':
            soma = soma + habitantes[i]['idade']
            homens_natacao += 1

        if homens_natacao == 0:
            return aviso()
        else:
            return f"A idade média de homens que fazem natação é: {soma /homens_natacao}"

habitantes = []
inicio()
print(respostas())

