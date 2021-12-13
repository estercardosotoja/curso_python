"""
1 - Crie duas linhas, uma para o carrinho do supermercado que irá receber produtos comprados e outra para os preços dos
produtos. Utilizando um loop, preencha as linhas com 5 produtos e 5 preços, recebendo estes dados do usuário (inout).
Por fim, some os preços, imprima o valor total e os produtos do carrinho.
"""

carrinho = []
precos = []
contprod = 0
valotTotal = 0
produto = ''

contprod = 1
while contprod < 6:
    produto = "produto"
    carrinho.append(produto)
    precos.append(contprod)
    contprod += 1

print(carrinho)
print(precos)

for id in range(0, 6):
    valotTotal += precos[id]

print(valotTotal)
