"""

1) Sami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil em um período de 6 meses,
até então Dudu já visitou o Espírito Santo e São Paulo, enquanto Sami visitou Rio de Janeiro e Bahia.
Crie dois conjuntos diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu
visitou Bahia, Acre, Santa Catarina e Sergipe, enquanto Sami visitou Bahia, Minas Gerais, Amazonas e Paraná,
atualize cada um dos conjuntos com os novos Estados. Responda:
"""

#Minha Resolução

Sami = {"Rio de Janeiro", "Bahia"}
Dudu = {"Espírito Santo", "São Paulo"}
resposta = ' '

adicionar_Dudu = input(f"Adicionar mais estados para Dudu? s/n ")
if adicionar_Dudu != 'n':
    while resposta != 'n':
        estado_adional = input("Estado adicional Dudu")
        Dudu.add(estado_adional)
        resposta = input('Adicionar mais estado para Dudu? S/N')

resposta = ' '
adicionar_Sami = input(f"Adicionar mais estados para Sami? s/n ")
if adicionar_Sami != 'n':
    while resposta != 'n':
        estado_adional = input("Estado adicional Sami")
        Sami.add(estado_adional)
        resposta = input('Adicionar mais estado para Sami? S/N')

print(f"\n Estados visitados por Dudu: {Dudu}"
      f"\n Estados visitados por Sami: {Sami}"
      f"\n Estados Dudu visitou que Sami não foi: {Dudu.difference(Sami)}"
      f"\n Estados Dudu e Sami visitaram: {Dudu.union(Sami)}")

porcentagem_Sami = ((len(Sami)*100)//27)
porcentagem_Dudu = ((len(Dudu)*100)//27)

if porcentagem_Sami < porcentagem_Dudu:
    print(f"Dudu venceu com {porcentagem_Dudu}%")
elif porcentagem_Sami > porcentagem_Dudu:
    print(f"Sami venceu com {porcentagem_Sami}%")
else:
    print(f"Empate \n Dudu: {porcentagem_Dudu} \n Sami: {porcentagem_Sami}")


# Resolução do Curso

#Situação inicial ao começar o desafio
estados_sami = {'RJ','BA'}
estados_dudu = {'ES','SP'}
sair = ''

while sair != 'nao':
    estados_sami.add(input('Qual Estado Sami visitou a mais? '))
    sair = input('Tem mais Estados a adicionar? ')


sair = ''
while sair != 'nao':
    estados_dudu.add(input('Qual Estado Dudu visitou a mais? '))
    sair = input('Tem mais Estados a adicionar? ')

    print(estados_dudu.difference(estados_sami))
    print(estados_sami.intersection(estados_dudu))
    if len(estados_sami) > len(estados_dudu):
        print(f'Sami ganhou e visitou {len(estados_sami)*100 // 27} %')
    elif len(estados_dudu) > len(estados_sami):
        print(f'Dudu ganhou e visitou {len(estados_dudu)*100 // 27} %')
    else:
        print(f'Deu empate e ambos visitaram  {len(estados_dudu)*100//27}%')
