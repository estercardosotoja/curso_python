"""
1 - Criar um arquivo de texto, inserir o lucro mensal de uma startup entre os
meses de janeiro e maio, informando o mês e o valor, através da entrada do
usuário. Após isso, ler o arquivo e imprimir o mês de maior lucro.
"""

relatorio = []
val = 0
mes = 0

# Escrever em arquivos com entrada de dados
with open('Aula86_EscreverEmArquivosExercicio.txt', 'w') as lucro:
        lucro.write("Jan: 10000\n")
        lucro.write("Fev: 40000\n")
        lucro.write("Mar: 800000\n")
        lucro.write("Abr: 15000\n")
        lucro.write("Mai: 90000\n")

lucro.close()

with open('Aula86_EscreverEmArquivosExercicio.txt') as LE:
    for linha in LE:
        relatorio[linha[0:3]] = int(linha[5:])  # A chave do dicionário é o mês (da
#    posição 0 até a 3), e o valor é o lucro (da posição 5 até o final da linha).
        print(relatorio)

    maiorLucro = 0
    mesMaiorLucro = ''

    for mes, lucro in relatorio.items():
        if lucro > maiorLucro:
            maiorLucro = lucro
        mesMaiorLucro = mes
    print(f'Mês com maior lucro: {mesMaiorLucro} com {maiorLucro} reais')

