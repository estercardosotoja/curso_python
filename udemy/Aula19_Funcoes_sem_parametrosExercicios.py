"""

    1) Foi realizada uma pesquisa de algumas características e gostos de quatro habitantes incluindo:
    nome, sexo, esporte favorito (Natação, Futebol, Volêi, Tênis) e idade. Com esses dados faça:
    - Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
    - Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam
    de natação chame uma função e imprima um aviso de que não há homens que gostam de natação

"""

#Minha solução

def questionario():
    dados = dict(nome=input("Nome do habitante:"),
                 sexo=str(input("Nome do sexo: m/f")),
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
    habitantes.append(questionario())
    sair = input("Adicionar mais alguém? s/n: ")
    if sair != "n":
        inicio()
    else:
        print(f"Fim \n Habitantes {habitantes}")

def aviso():
    return "Não há homens que gostam de natação"

def respostas():
    total = len(habitantes)
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


#Solução do Curso:

def cadastro(): #Função que realiza a criação da lista com os dados
 list = []
 for i in range(4):
    dicionario = dict(nome = input('Digite seu nome: '),
                      sexo = input('Digite M para masculino e F para feminino: '),
                      esporte = input('Escolha seu esporte favorito entre natacao, futebol, volei, tenis: '),
                      idade = int(input('Digite sua idade: ')))
    list.append(dicionario) #Adiciona o dicionario na lista
    return list #retorna a lista

def aviso(): #Mensagem de que não existem homens que gostam de natacao
 print('Nao tem homens que gostam de natacao')
 lista = cadastro()
 cont = 0 #Contar quantos homens gostam de natação
 soma = 0 #Fazer a soma do numerador para calcular a media
 for i in range(4):
    if lista[i]['sexo'] == 'M' and lista[i]['esporte'] == 'natacao':
        soma = soma + lista[i]['idade']
        cont += 1
 if cont == 0:
    aviso()
 else:
    media = soma / cont #Calcula a media
    print(f'A idade media de homens que fazem natacao é {media}')