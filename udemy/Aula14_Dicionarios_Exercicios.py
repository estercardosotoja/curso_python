"""
1) Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
- Crie um dicionário chamado herói com chave sendo o nome do personagem e o elemento o nível de poder do personagem
entre 1 a 100. Ex: herói = {‘Flash’:85}.

- Crie outro dicionário que serão as armas que podem ser usadas pelo herói, sendo a chave o nome da arma e
 o elemento o nível de poder de 0 a 100. Ex: arma = {‘Escudo do Capitão América’:60}

- Crie um último dicionário representado os vilões sendo a chave o nome e o elemento o nível de poder de 0 a 200.
Ex: vilao={‘Thanos’:175}

Após isso o usuário poderá escolher um herói, uma arma soma os pontos de poder e escolher um vilao para lutar,
apresente quem foi o vencedor, caso for o herói imprima a arma usada. Caso resulte em empate informe na saída.
Observação: Pode definir qualquer herói,vilao e arma que quiser
"""


heroes = {
    "Flash": 90,
    "Homem Aranha": 70,
    "Homem de Ferro": 90,
    "SuperMan": 98,
    "Mulher Maravilha": 97,
    "Arqueiro": 70,
    "Batman": 68
}

elements = {
    "arco-flecha": 50,
    "lanca-teia": 45,
    "laco-da-verdade": 56,
    "armadura": 95,
    "batmovel": 60
}

villains = {
    "Zoom": 105,
    "Doutor Octopus": 125,
    "Chicote Negro": 130,
    "Lex Luthor": 150,
    "Maxwell Lord": 120,
    "Exterminador": 180,
    "Curinga": 160,
}

#Escolha do usuario
heroi_escolhido = input('Digite o heroi escolhido: ')
arma_escolhida = input('Digite a arma escolhida: ')
vilao_escolhido = input('Digite o vilao escolhido: ')

soma_dos_poderes = (heroes.get(heroi_escolhido) + elements.get(arma_escolhida))

if soma_dos_poderes > villains.get(vilao_escolhido):
    print(f'O vencedor é {heroi_escolhido} com {arma_escolhida}')
elif soma_dos_poderes == villains.get(vilao_escolhido):
    print(f'Logo, logo teremos outro confronto! Esse deu empate')
else:
    print(f'Ovencedor é {vilao_escolhido}, deu ruim')
