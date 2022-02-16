"""
1) Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente em cima da hora.
Ele resolveu comprar um tipo de flor, um presente e escolher um lugar para saírem, ele anotou todas as opções abaixo:

        Flores
Tipo                Preço
Rosas Vermelhas     145,00
Girassóis           125,00
Margaridas          120,00
Flores do campo     140,00

        Presente
Tipo                Preço
Urso de Pelúcia     55,00
Caixa de Bombom     60,00
Colar               75,00
Roupas              40,00

        Lugar
Tipo                Preço
Praia               70,00
Sair para jantar    150,00
Parque de diversões 120,00
Hotel               180,00

- Crie um programa que descubra qual a combinação mais cara, em seguida mais barata e a média opção.
    Imprima a combinação em cada caso.
- Use um dicionário para cada item (flor, lugar e presente).
"""


""" Minha Versão """
flores = {
    "Rosas Vermelhas": 145.00, "Margaridas": 120.00, "Girassóis": 125.00, "Flores do campo": 140.00
}
presentes = {
    "Urso de Pelúcia ": 55.00, "Caixa de Bombom": 60.00, "Colar": 75.00, "Roupas": 40.00
}
lugares = {
    "Praia": 70.00, "Sair para jantar": 150.00, "Parque de diversões": 120.00, "Hotel": 180.00
}

flor_Cara = 0
for flor in flores:
    if flores[flor] > flor_Cara:
        flor_Cara = flores[flor]
        itens_Caro = {flores[flor], flor}
print(f"Flor mais cara é a {flor} e custa R$ {flor_Cara}  "
      f"\n Itens Caros: {itens_Caro} ")


flor_Barata = flores[flor]
for flor in flores:
    if flores[flor] < flor_Barata:
        flor_Barata = flores[flor]
        itens_Barato = {flores[flor], flor}
print(f"Flor mais barata é a {flor} e custa R$ {flor_Barata} "
      f"\n Itens Baratos : {itens_Barato}")

presente_Caro = 0
for item in presentes:
    if presentes[item] > presente_Caro:
        presente_Caro = presentes[item]
        itens_Caro = {item, presentes[item]}
print(f"Presente Caro = {presente_Caro} "
      f"\n Itens Caros: {itens_Caro} ")

presente_Barato = presentes[item]
for item in presentes:
    if presentes[item] < presente_Caro:
        presente_Caro = presentes[item]
        itens_Barato = {item, presentes[item]}
print(f"Presente Barato = {presente_Barato}"
      f"\n Itens Baratos : {itens_Barato}")

lugar_Caro = 0
for lugar in lugares:
    if lugares[lugar] > lugar_Caro:
        lugar_Caro = lugares[lugar]
        itens_Caro = {lugares[lugar], lugar}
print(f"Lugar Caro = {lugar_Caro} "
      f"\n Itens Caros: {itens_Caro} ")

lugar_Barato = lugares[lugar]
for lugar in lugares:
    if lugares[lugar] < lugar_Barato:
        lugar_Barato = lugares[lugar]
        itens_Barato = {lugares[lugar], lugar}
print(f"Lugar Barato = {lugar_Barato}"
      f"\n Itens Baratos : {itens_Barato}")

menorValor = flor_Barata + presente_Barato + lugar_Barato
maiorValor = flor_Cara + presente_Caro + lugar_Caro

""" Versão do Curso """

#Declaração dos dicionários
flores ={'Rosas Vermelhas':145,'Girassóis':125,'Margarida':120,'Flores do campo':140}
presentes = {'Urso de pelucia':55,'Caixa de bombom':60, 'Colar':75, 'Roupas':40}
lugares = {'Praia':70,'Sair para jantar':150,'Parque de Diversao':120, 'Hotel':180}

#Encontrando a combinação mais cara:
#Inicializando variaveis
preco_total = 0
flor_cara = ''
presente_caro = ''
lugar_caro = ''
for flor,valor in flores.items(): #A função items() retorna a chave e
                                  #valor como lista de tuplas
    for presente,preco in presentes.items():
        for lugar,custo in lugares.items():
            preco_atual = valor + preco + custo
            if preco_atual > preco_total: #Se o preco atual for maior
                                          #que o preco total faça:
                preco_total = preco_atual
                flor_cara = flor
                presente_caro = presente
                lugar_caro = lugar
#Imprime a combinação mais cara
print(f'Custo total:{preco_total}, Flor:{flor_cara}, Presente:{presente_caro}, Lugar:{lugar_caro}')

#Encontrando a combinação mais barata:
#aux é uma Variavel auxiliar para inicializar preco total, pois se colocar preco_total = 0 não tem como fazer a comparação dentro no if
aux = 0
preco_total = 0
flor_barata = ''
presente_barato = ''
lugar_barato = ''
for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar,custo in lugares.items():
            if aux == 0: #Se aux for zero inicializa preco_total
                preco_total = valor + preco + custo
                aux +=1
            else: #Se não faça:
                preco_atual = valor + preco + custo
                if preco_total > preco_atual:
                    preco_total = preco_atual
                    flor_barata = flor
                    presente_barato = presente
                    lugar_barato = lugar
#Imprime o menor custo
print(f'Custo total:{preco_total}, Flor:{flor_barata}, Presente:{presente_barato}, Lugar:{lugar_barato}')

#Achando a média opção de preço: Obs: Há duas possibilidades
preco_total = 0
list = [] #Lista que armazena todas as possibilidades de preços dentro
          #dos dicionarios
for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar,custo in lugares.items():
            #Adiciona a soma de cada combinação dentro da lista
            list.append(valor + preco + custo)
list.sort() #Organiza a lista do menor para maior elemento
preco_total = list[len(list) // 2] #Pega o valor do elemento central e
                                   #armazena para preco_total

for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar,custo in lugares.items():
            if valor + preco + custo == preco_total:
                #Imprime o custo e combinação da opção de preço médio
                print(f'Custo total:{preco_total}, Flor:{flor}, Presente:{presente}, Lugar:{lugar}')
