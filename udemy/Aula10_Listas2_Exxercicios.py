"""
1 - Criar um sistema de comando de uma loja de jogos. O programa deve conter pelo menos 6 listas:
uma indicando quais jogos estão disponíveis para venda,
uma para mostrar o preço de cada jogo,
uma para mostrar a quantidade de jogos disponíveis na loja para venda,
uma informando o preço de fábrica dos jogos para aumentar o estoque,
uma para registrar as vendas e uma para registrar as compras de estoque.
Todas as informações de um jogo devem estar no mesmo índice nas listas.
Criar um menu interativo com as seguintes opções para o usuário:
Registrar venda, Compra de estoque, Resumo da loja, Sair.
Ao sair indicar que o caixa está fechado.
O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque,
sem esquecer de alterar os valores da lista de quantidade.
"""

dispo = ['Sonic', 'Velocidade Máxima', 'Naruto', 'GTA', 'Far Cry']
precoVenda = [210.99, 123.45, 156.87, 234.12, 342.56]
precosCompraEstoque = [105.00, 1.50, 75.00, 0.90, 62.50] #Preços para o dono da loja comprar da fábrica
quantidade = [3, 0, 2, 5, 1] #Quantidade de jogos disponíveis
vendas = [] #Vendas registradas
compraDeEstoque = [] #Compras de estoque registradas
opcao = 0

while opcao != 4:
    print(" ======== LOJAS DE JOGOS ======= ")
    opcao = int(input(f'\t 1 - Registrar Venda '
                      f'\n \t 2 - Comprar de Estoque '
                      f'\n \t 3 - Resumo da Loja '
                      f'\n \t 4 - Sair '
                      f'\n \t Digite a opção: '))
    if opcao == 1:
        jogoVendido = input('Jogo Vendido: ')
        quantidadeVendida = int(input('Quantidade vendida: '))
        if quantidadeVendida <= quantidade[dispo.index(jogoVendido)]:
            print(f'\n{jogoVendido} Vendido !')
            quantidade[dispo.index(jogoVendido)] -= quantidadeVendida
            vendas.append(precoVenda[dispo.index(jogoVendido)] * quantidadeVendida)
        else:
            print('Não há jogo suficiente para ser vendido')
    elif opcao == 2:
        jogoComprado = input('Jogo Comprado: ')
        quantidadeComprado = int(input('Quantidade comprada: '))
        print(f'\n {jogoComprado} Comprado !')
        quantidade[dispo.index(jogoComprado)] += quantidadeComprado
        compraDeEstoque.append(precosCompraEstoque[dispo.index(jogoComprado)] * quantidadeComprado)
    elif opcao == 3:
        print("--------------------- Resumo dos Produtos: ---------------------")
        print(f'\t Indice \t Jogo \t  Quantidade \t \t Valor de Venda \t \t  ValorForncedor')
        for indices, jogo in enumerate(dispo):
            print(f'\t {indices} \t \t| '
                  f'\t {dispo[indices]} \t \t| '
                  f'\t {quantidade[indices]} \t| '
                  f'\t {precoVenda[indices]} \t| '
                  f'\t {precosCompraEstoque[indices]}')
        print(f' Lucros: R${sum(vendas)}')
        print(f'Soma de Produtos: R$ {sum(precoVenda)}')
        print(f'Soma de Valor Investido: R${sum(precosCompraEstoque)}')
        print(f'Produto mais caro da Loja: R${max(precoVenda)}')
        print(f'Produto de menor valor da Loja: R${min(precoVenda)}')
    elif opcao == 4:
        print('Foi uma prazer até a próxima \o/')
        opcao = 4
    else:
        print('Opcao Invalida')
